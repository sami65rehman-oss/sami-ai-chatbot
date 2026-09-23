import streamlit as st
from logic import get_ai_response

st.set_page_config(page_title="Sami.AI", page_icon="🤖")

st.title("🤖 Sami.AI")
st.caption("AI Assistant powered by Groq & Llama 3")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle User Input
if prompt := st.chat_input("Ask Sami.AI..."):
    # Add user message to UI & session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from AI logic file
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # Format messages history for Groq
            formatted_history = [
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ]
            
            # Call logic.py function
            reply = get_ai_response(formatted_history)
            st.markdown(reply)
            
    # Save assistant response to session state
    st.session_state.messages.append({"role": "assistant", "content": reply})