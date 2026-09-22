import streamlit as st
from logic import client, get_chat_response

st.set_page_config(page_title="Sami.AI", page_icon="🤖")

st.title("🤖 Sami.AI")
st.caption("AI Assistant powered by Gemini 3.6 Flash")

if "chat" not in st.session_state:
    st.session_state.chat = client.chats.create(model="gemini-3.6-flash")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Hello, I am Sami.AI. How can I help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_generator = get_chat_response(st.session_state.chat, prompt)
        response_text = st.write_stream(response_generator)
    
    st.session_state.messages.append({"role": "assistant", "content": response_text})