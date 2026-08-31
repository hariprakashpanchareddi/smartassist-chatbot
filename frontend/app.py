import streamlit as st
import requests
import uuid
st.set_page_config(page_title="SmartAssist Chat", page_icon="🤖")
st.title("SmartAssist Support 🤖")
API_URL = "http://127.0.0.1:8000/chat"
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())
if "messages" not in st.session_state:
    st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
if prompt := st.chat_input("How can I help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                res = requests.post(API_URL, json={"session_id": st.session_state.session_id, "message": prompt})
                reply = res.json()["response"] if res.status_code == 200 else "API Error."
            except:
                reply = "Backend not running."
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
