import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')

if not api_key:
    print("Error: API key not found in .env")
else:
    print(f"API key loaded successfully! Length: {len(api_key)}")
    try:
        # Initialize the modern SDK client
        client = genai.Client(api_key=api_key)
        
        # Test a simple generation
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents='Say the word "Success!"'
        )
        print(f"Gemini Response: {response.text.strip()}")
        print("=== Gemini API Setup Successful ===")
    except Exception as e:
        print(f"API Error: {e}")
