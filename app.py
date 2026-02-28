import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="Infinity AI ♾️", layout="wide")

# Sidebar for API Key
st.sidebar.title("Infinity AI ♾️")
api_key = st.sidebar.text_input("Gemini API Key daalein:", type="password")
uploaded_file = st.sidebar.file_uploader("Trading Chart upload karein", type=['png', 'jpg', 'jpeg'])

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-pro')

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Kaise madad karu?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            if uploaded_file:
                img = Image.open(uploaded_file)
                # SMC Specialist prompt
                full_prompt = f"Analyze this trading chart strictly using Smart Money Concepts (SMC). Question: {prompt}"
                response = model.generate_content([full_prompt, img])
            else:
                response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
          
