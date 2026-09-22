import streamlit as st
from logic import get_ai_response
st.set_page_config(
    page_title="Sami.AI", page_icon="🤖", layout="centered"
)
st.title("🤖 Sami.AI")
st.caption("World Best AI ASSISTANCE  | Powered by Gemini 3.6 Flash")
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "assistant",
            "content": "Salam i am Sami.AI, a Gemini 3.6 Flash model based AI assistant. How can i help you today?",
        }
    ]
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
user_prompt = st.chat_input("what you want to ask me?")
if user_prompt:
    with st.chat_message("user"):
        st.write(user_prompt)
    st.session_state["messages"].append(
        {"role": "user", "content": user_prompt}
    )
    with st.chat_message("assistant"):
        ai_reply = st.write_stream(get_ai_response(user_prompt))
    st.session_state["messages"].append(
        {"role": "assistant", "content": ai_reply}
    )