from fastapi import FastAPI

app = FastAPI(title="SmartAssist Chatbot API")

@app.get("/")
def read_root():
    return {"status": "SmartAssist API is running"}

@app.post("/chat")
def chat(message: str):
    # Day 1: Simple echo response
    return {"response": f"Echo: {message}"}
