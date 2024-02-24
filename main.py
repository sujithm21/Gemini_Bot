# Importing the dependencies
import os
import streamlit as st
import google.generativeai as gen_ai
from dotenv import load_dotenv

#Loading the environment variables
load_dotenv()

#Configure streamlit page settings 
st.set_page_config(page_title='The Ultimate Bot', page_icon=':Goblin:',layout="centered")

#API key
GOOLE_API_KEY = os.getenv("GOOGLE_API_KEY")

#Set AI model
gen_ai.configure(api_key=GOOLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

#Function to translate roles b/w streamlit and gemini
#To uniformize the convenction b/w streamlit and gemini pro
def translate_role(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role
    

#Initialize the chat session if it is not present in streamlit
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

#Display the chat bot heading 
st.title("🫡Geminiiii Botttt!")

# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role(message.role)):
        st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("Ask Gemini-Pro...")
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)