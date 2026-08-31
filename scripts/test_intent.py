from app.services.intent import classify_intent

test_queries = [
    "Hello there! Good morning.",
    "I am extremely frustrated and want to speak to a manager.",
    "My webhook integration is throwing a 500 error.",
    "This service is terrible and I hate it.",
    "How do I upgrade my billing plan?"
]

print("=== Testing Intent Classification ===")
for query in test_queries:
    intent = classify_intent(query)
    print(f"Query: '{query}'")
    print(f"--> Intent: {intent.upper()}\n")
