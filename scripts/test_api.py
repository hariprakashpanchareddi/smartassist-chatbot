from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

print("=== Testing FastAPI Endpoints ===")

print("\n1. Testing GET /health ...")
response = client.get("/health")
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.json()}")

print("\n2. Testing POST /chat ...")
payload = {"message": "Hello, I need some help."}
response = client.post("/chat", json=payload)
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.json()}")
