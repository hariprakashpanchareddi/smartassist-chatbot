from app.services.memory import init_db, save_message, get_recent_history

print("=== 1. Initializing DB ===")
init_db()

session_id = "test_user_session_101"

print("\n=== 2. Storing Conversation Turns ===")
save_message(session_id, "user", "Hi, I need help with my account.")
save_message(session_id, "assistant", "Hello! What account issue are you facing?")
save_message(session_id, "user", "I want to change my email address.")
save_message(session_id, "assistant", "You can update your email under profile settings.")
save_message(session_id, "user", "What about resetting my password?")
save_message(session_id, "assistant", "Use the reset password link on the login page.")

print("\n=== 3. Retrieving Sliding Window Context (Last 4 messages) ===")
recent = get_recent_history(session_id, limit=4)
for msg in recent:
    print(f"[{msg['role'].upper()}]: {msg['content']}")
