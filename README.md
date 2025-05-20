# Gemini Web Search Assistant 🔎

This project is an AI-powered assistant built using Google Gemini (via OpenAI-compatible API), LangChain, and Serper.dev for live web search. The assistant uses a custom tool to perform real-time searches using Google's results.

## 💡 Features

- Google-like web search powered by Serper API
- Gemini Flash model integration via OpenAI-compatible endpoint
- Streamlit interface for easy interaction
- Async architecture for responsive performance

## Install Requirements
Make sure you have Python 3.8+ installed.

pip install -r requirements.txt

## Set Up Environment Variables
Create a .env file in the root directory and add your API keys:

# .env
GEMINI_API_KEY=your_gemini_api_key_here
SERPER_API_KEY=your_serper_api_key_here
