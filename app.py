import streamlit as st
from openai import OpenAI

# Direct API key paste (⚠️ not safe if you share code)
client = OpenAI(api_key="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")

st.title("SmartStudy AI Chatbot")

# Initialize messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful study assistant."}
    ]

# User input
user_input = st.text_input("Ask me anything:")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Call OpenAI API
    resp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages
    )

    reply = resp.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})

    # Show reply
    st.write("**Assistant:**", reply)
