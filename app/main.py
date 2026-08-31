from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.services.bot import process_message
import uuid

app = FastAPI(title="SmartAssist API", description="API for the SmartAssist Customer Support Chatbot")

class ChatRequest(BaseModel):
    session_id: str | None = None
    message: str

class ChatResponse(BaseModel):
    session_id: str
    response: str

@app.get("/health")
async def health_check():
    """Health check endpoint to verify the API is running."""
    return {"status": "healthy"}

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Main chat endpoint. Receives a user message, processes it via the RAG/LLM pipeline,
    and returns the assistant's response.
    """
    try:
        # Generate a new session ID if one wasn't provided
        session_id = request.session_id or str(uuid.uuid4())
        
        # Process the message through our orchestrator
        bot_response = process_message(session_id, request.message)
        
        return ChatResponse(session_id=session_id, response=bot_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
