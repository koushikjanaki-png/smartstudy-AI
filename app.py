import streamlit as st
import openai

# --- Set your OpenAI API key here ---
# It's safer to use Streamlit secrets or environment variables
openai.api_key = "YOUR_OPENAI_API_KEY_HERE"

# --- Function to get response from OpenAI ---
def get_openai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']
    except openai.error.AuthenticationError:
        return "Authentication Error: Check your API key!"
    except openai.error.APIError as e:
        return f"OpenAI API Error: {e}"
    except Exception as e:
        return f"Unexpected Error: {e}"

# --- Streamlit UI ---
st.title("SmartStudy AI Chatbot")

user_input = st.text_input("Enter your message:")

if st.button("Send"):
    if user_input:
        reply = get_openai_response(user_input)
        st.text_area("ChatGPT Reply:", value=reply, height=200)
