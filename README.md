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

📌 Where to Get These Keys?
## GEMINI_API_KEY:
Go to [https://aistudio.google.com/app/apikey](Google AI Studio) and create your API key.

## SERPER_API_KEY:
Sign up at https://serper.dev → Go to your dashboard → Copy your API key.


## Run the Streamlit Interface
streamlit run ui.py

You will see a browser window open with a text box where you can enter queries like:

Search for current temperature in Karachi

Find top 5 news about OpenAI

Search tourist places in Japan

## Expected Output
The assistant will call the Serper API in the background and return summarized results with source URLs.

If the SERPER_API_KEY is not set correctly, you will see a configuration error in the output.
