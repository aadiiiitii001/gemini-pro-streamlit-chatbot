import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.title("AI Chat App (Auto Model Selection)")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- Step 1: Determine available models ---
if "model_name" not in st.session_state:
    available_models = genai.list_models()
    model_name = None

    # Prefer chat model
    for m in available_models:
        if "generate_message" in m.supported_methods:
            model_name = m.name
            st.session_state.model_type = "chat"
            break

    # Fallback to content generation
    if not model_name:
        for m in available_models:
            if "generate_content" in m.supported_methods:
                model_name = m.name
                st.session_state.model_type = "content"
                break

    if not model_name:
        st.error("No compatible model available for your account.")
    else:
        st.session_state.model_name = model_name
        st.info(f"Using model: {model_name}")

# User input
user_prompt = st.text_input("Enter your message:")

if st.button("Send") and user_prompt and "model_name" in st.session_state:
    messages = st.session_state.chat_history.copy()
    messages.append({"role": "user", "content": user_prompt})

    # Generate AI response based on model type
    if st.session_state.model_type == "chat":
        model = genai.ChatModel(st.session_state.model_name)
        response = model.generate_message(messages=messages)
        ai_reply = response.last.content[0].text
    else:  # content generation fallback
        model = genai.GenerativeModel(st.session_state.model_name)
        # For content models, send only user messages as list of strings
        contents = [msg["content"] for msg in messages if msg["role"] == "user"]
        response = model.generate_content(contents=contents)
        ai_reply = response.result[0].content[0].text

    # Update chat history
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})
    st.session_state.chat_history.append({"role": "assistant", "content": ai_reply})

# Display chat history
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f"**You:** {chat['content']}")
    else:
        st.markdown(f"**AI:** {chat['content']}")
