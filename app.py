import streamlit as st
import openai

# ---------------------------
# STEP 1: Set your OpenAI API key
# ---------------------------
openai.api_key = "YOUR_OPENAI_API_KEY"  # <- Replace this with your actual key

# ---------------------------
# STEP 2: Function to get response from OpenAI
# ---------------------------
def get_openai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']
    except openai.error.AuthenticationError:
        return "Authentication Error: Check your API key!"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# ---------------------------
# STEP 3: Streamlit UI
# ---------------------------
st.set_page_config(page_title="SmartStudy AI Chatbot", page_icon="🤖")
st.title("SmartStudy AI Chatbot")

# Initialize session state to store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("You:", key="input")

if st.button("Send"):
    if user_input:
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
        st.markdown(f"**AI:** {msg['content']}")
