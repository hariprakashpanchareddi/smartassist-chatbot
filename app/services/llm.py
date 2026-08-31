import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

def generate_response(query: str, context_docs: list[dict]) -> str:
    """
    Generates a chatbot response using the Gemini API and RAG context.
    """
    if not context_docs:
        context_text = "No relevant knowledge base articles found."
    else:
        context_text = "\n\n".join([f"--- {doc['metadata']['source']} ---\n{doc['content']}" for doc in context_docs])
        
    prompt = f"""You are SmartAssist, a helpful and professional customer support chatbot.
Use ONLY the information in the Knowledge Base provided below to answer the User Query.
If the answer is not contained in the Knowledge Base, apologize and state that you cannot help with that specific issue, and offer to connect them to a human agent. Do not invent information.

Knowledge Base:
{context_text}

User Query: {query}

Response:"""

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )
    return response.text.strip()
