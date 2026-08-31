from app.services.intent import classify_intent
from app.services.rag import retrieve_context
from app.services.llm import generate_response
from app.services.memory import save_message, get_recent_history

def process_message(session_id: str, user_text: str) -> str:
    """
    Main orchestrator: handles intent routing, memory, RAG, and LLM generation.
    """
    # 1. Save user input
    save_message(session_id, "user", user_text)
    
    # 2. Classify intent
    intent = classify_intent(user_text)
    
    # 3. Handle specific intents without LLM/RAG if needed
    if intent == "greeting":
        response = "Hello! I am SmartAssist. How can I help you today?"
    elif intent == "escalation":
        response = "I understand you'd like to speak with a human. Transferring you to our support team..."
    elif intent == "complaint":
        response = "I apologize that you're having a poor experience. Let me connect you with an agent who can help."
    else:
        # 4. Handle FAQ and Technical intents via RAG
        # Fetch relevant documents
        docs = retrieve_context(user_text, top_k=2)
        
        # Fetch conversation history for context (optional enhancement for the prompt later, 
        # but required to track state)
        history = get_recent_history(session_id, limit=4)
        
        # Generate LLM response based on knowledge base
        response = generate_response(user_text, docs)
        
    # 5. Save assistant response
    save_message(session_id, "assistant", response)
    
    return response
