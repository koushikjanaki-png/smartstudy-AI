import streamlit as st
import openai

# Load the key from secrets
openai.api_key = st.secrets["OPENAI_KEY"]

# Example usage
try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello!"}]
    )
    st.write(response.choices[0].message["content"])
except openai.error.AuthenticationError:
    st.error("Authentication Error: Check your OpenAI API key!")
