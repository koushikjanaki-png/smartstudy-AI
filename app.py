# app.py
import streamlit as st
import openai

# -------------------------------
# 1️⃣ Directly set OpenAI API key (local testing ONLY)
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxx"  # Replace with your new key

# -------------------------------
# 2️⃣ Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------
# 3️⃣ Streamlit UI
st.title("Smart Study Chatbot 🤖")

user_input = st.text_input("Ask me anything:")

if user_input:
    # Add user message to session
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Call OpenAI ChatCompletion API
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        bot_message = response.choices[0].message["content"]
        st.session_state.messages.append({"role": "assistant", "content": bot_message})
    except openai.error.AuthenticationError:
        st.error("Authentication Error: Check your OpenAI API key!")
    except Exception as e:
        st.error(f"Error: {e}")

# -------------------------------
# 4️⃣ Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")
