import streamlit as st
import google.generativeai as genai

# Configure API key
genai.configure(api_key="YOUR_API_KEY")  # Replace with your actual API key

st.title("My AI Chat App")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_prompt = st.text_input("Enter your message:")

if st.button("Send") and user_prompt:
    # Use a valid model: chat-bison
    model = genai.GenerativeModel("chat-bison")  

    # Send message to the model
    response = model.generate_content(
        contents=st.session_state.chat_history + [{"type": "text", "text": user_prompt}],
    )

    # Extract model's reply
    ai_reply = response.result[0].content[0].text

    # Store in chat history
    st.session_state.chat_history.append({"type": "user", "text": user_prompt})
    st.session_state.chat_history.append({"type": "ai", "text": ai_reply})

# Display chat
for chat in st.session_state.chat_history:
    if chat["type"] == "user":
        st.markdown(f"**You:** {chat['text']}")
    else:
        st.markdown(f"**AI:** {chat['text']}")
