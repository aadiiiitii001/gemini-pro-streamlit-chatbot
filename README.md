Gemini-Pro Streamlit Chatbot

An interactive AI chatbot built using Google Gemini-Pro API and Streamlit, enabling real-time conversational experiences with multimodal capabilities (text and image).

🚀 Features

💬 Chat with Gemini Pro (Text) model

🖼️ Optional support for Gemini Pro Vision (Text + Image)

⚡ Real-time streaming responses

🎨 Clean and modern Streamlit UI

💾 Chat history with context memory

☁️ Deployable on Render, Hugging Face Spaces, or Streamlit Cloud

🧠 Tech Stack
Component	Description
Frontend	Streamlit
Backend	Python
AI Model	Google Gemini Pro / Gemini Pro Vision
API Integration	google-generativeai SDK
Deployment	Render / Streamlit Cloud / Hugging Face Spaces
📦 Installation

Clone the repository

git clone https://github.com/<your-username>/gemini-pro-streamlit-chatbot.git
cd gemini-pro-streamlit-chatbot


Create a virtual environment

python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows


Install dependencies

pip install -r requirements.txt


Set up environment variables

Create a .env file in the project root:

GEMINI_API_KEY=your_google_gemini_api_key

🧾 Example requirements.txt
streamlit
python-dotenv
google-generativeai
Pillow

▶️ Run the App
streamlit run app.py


Then open the URL shown in the terminal, usually:
👉 http://localhost:8501
