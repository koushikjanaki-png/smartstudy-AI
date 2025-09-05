# app.py
import streamlit as st
import openai

# ----------------------------
# Set your OpenAI API key here
# ----------------------------
# Option 1: Directly in code (not recommended for public apps)
# openai.api_key = "YOUR_API_KEY"

# Option 2: Use environment variable (better)
# Make sure OPENAI_API_KEY is set in your system or Streamlit secrets
openai.api_key = st.secrets.get("OPENAI_API_KEY")  # Recommended

# ----------------------------
# Streamlit App
# ----------------------------
st.set_page_config(page_title="SmartStudy Chatbot", page_icon="🤖")
st.title("🤖 SmartStudy Chatbot")

# Initialize session state for chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("Type your message here:", key="input")

# Function to get OpenAI response
def get_openai_response(user_message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can also use gpt-4 if available
            messages=st.session_state.messages + [{"role": "user", "content": user_message}],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content
    except openai.errors.AuthenticationError as e:
        return "Authentication failed. Please check your API key."
    except openai.errors.RateLimitError as e:
        return "Rate limit exceeded. Please try again later."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Send button
if st.button("Send") and user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Get AI response
    reply = get_openai_response(user_input)
    
    # Add AI response to chat history
    st.session_state.messages.append({"role": "assistant", "content": reply})

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")
