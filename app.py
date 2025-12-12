import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.title("AI Chat App")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_prompt = st.text_input("Enter your message:")

if st.button("Send") and user_prompt:
    model = genai.GenerativeModel("text-bison-001")

    # Prepare messages as a list of strings (user messages only)
    messages = [chat["content"] for chat in st.session_state.chat_history if chat["role"] == "user"]
    messages.append(user_prompt)

    response = model.generate_content(contents=messages)
    ai_reply = response.result[0].content[0].text

    st.session_state.chat_history.append({"role": "user", "content": user_prompt})
    st.session_state.chat_history.append({"role": "assistant", "content": ai_reply})

for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f"**You:** {chat['content']}")
    else:
        st.markdown(f"**AI:** {chat['content']}")
