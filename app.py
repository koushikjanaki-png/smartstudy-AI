# app.py

import streamlit as st
import openai
from openai.error import AuthenticationError, RateLimitError, APIError

# ---- Set your OpenAI API key here ----
openai.api_key = "sk-YourActualKeyHere"  # Replace with your actual key

# Streamlit title
st.title("Smart Study AI Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("Ask me anything:")

def get_openai_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        return response['choices'][0]['message']['content']
    except AuthenticationError:
        return "❌ Authentication failed. Check your API key!"
    except RateLimitError:
        return "⚠️ Rate limit exceeded. Try again later."
    except APIError as e:
        return f"❌ OpenAI API error: {str(e)}"
    except Exception as e:
        return f"❌ Unexpected error: {str(e)}"

# Process user input
if user_input:
    reply = get_openai_response(user_input)
    st.session_state.messages.append({"user": user_input, "bot": reply})

# Display chat history
for msg in st.session_state.messages:
    st.markdown(f"**You:** {msg['user']}")
    st.markdown(f"**Bot:** {msg['bot']}")
