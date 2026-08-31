#!/bin/bash
echo "=== Starting SmartAssist Full Stack ==="

# 1. Start FastAPI in the background
PYTHONPATH=. PYTHONUNBUFFERED=1 uvicorn app.main:app --host 127.0.0.1 --port 8000 > server.log 2>&1 &
BACKEND_PID=$!

echo "Backend starting. Waiting 5 seconds..."
sleep 5

# 2. Start Streamlit in the foreground
echo "Starting Streamlit UI..."
streamlit run frontend/app.py

# 3. Cleanup backend when Streamlit is closed (Ctrl+C)
kill $BACKEND_PID
echo "Full stack shut down cleanly."
