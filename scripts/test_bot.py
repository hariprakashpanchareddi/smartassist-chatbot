from app.services.bot import process_message

session = "end_to_end_test_1"

print("=== Testing End-to-End SmartAssist Flow ===")

queries = [
    "Hello there!",
    "How do I reset my password?",
    "This is ridiculous, get me a human agent right now."
]

for query in queries:
    print(f"\n[USER]: {query}")
    response = process_message(session, query)
    print(f"[SMARTASSIST]: {response}")
