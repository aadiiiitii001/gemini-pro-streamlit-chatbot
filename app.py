import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Configure API key from environment variable
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.title("AI Chat App")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_prompt = st.text_input("Enter your message:")

if st.button("Send") and user_prompt:
    # Use chat-bison-001 for conversation
    model = genai.ChatModel("chat-bison-001")

    # Prepare messages for context (role + content)
    messages = st.session_state.chat_history.copy()
    messages.append({"role": "user", "content": user_prompt})

    # Generate AI response
    response = model.generate_message(messages=messages)
    ai_reply = response.last.content[0].text

    # Update chat history
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})
    st.session_state.chat_history.append({"role": "assistant", "content": ai_reply})

# Display chat history
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f"**You:** {chat['content']}")
    else:
        st.markdown(f"**AI:** {chat['content']}")
