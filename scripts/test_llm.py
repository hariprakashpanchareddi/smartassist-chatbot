from app.services.rag import retrieve_context
from app.services.llm import generate_response

query = 'How do I reset my password?'
print(f'User Query: {query}')

print('\n1. Retrieving context from ChromaDB...')
docs = retrieve_context(query, top_k=2)
print(f'Found {len(docs)} documents.')

print('\n2. Generating LLM response with gemini-2.5-flash...')
response = generate_response(query, docs)

print('\n=== SmartAssist Response ===')
print(response)
