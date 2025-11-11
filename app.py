import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Configure API key from environment variable
genai.configure(api_key=os.getenv("AIzaSyD_YourRealAPIKeyHere"))

st.title("My AI Chat App")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_prompt = st.text_input("Enter your message:")

if st.button("Send") and user_prompt:
    # Use a valid model
    model = genai.GenerativeModel("chat-bison")

    # Prepare messages as TextPrompt objects
    messages = [genai.TextPrompt(text=chat["text"]) for chat in st.session_state.chat_history]
    messages.append(genai.TextPrompt(text=user_prompt))  # Add current user input

    # Generate AI response
    response = model.generate_content(contents=messages)

    # Extract AI's text reply
    ai_reply = response.result[0].content[0].text

    # Update chat history
    st.session_state.chat_history.append({"type": "user", "text": user_prompt})
    st.session_state.chat_history.append({"type": "ai", "text": ai_reply})

# Display chat history
for chat in st.session_state.chat_history:
    if chat["type"] == "user":
        st.markdown(f"**You:** {chat['text']}")
    else:
        st.markdown(f"**AI:** {chat['text']}")
