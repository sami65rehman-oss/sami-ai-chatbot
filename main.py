import streamlit as st
from logic import get_gemini_response

st.set_page_config(page_title="Sami.AI", page_icon="🤖")

st.title("🤖 Sami.AI")
st.caption("World Best AI ASSISTANT | Powered by Gemini 2.5 Flash")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Salam, i am Sami.Ai. How can i help you?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_generator = get_gemini_response(prompt)
        response_text = st.write_stream(response_generator)
    
    st.session_state.messages.append({"role": "assistant", "content": response_text})