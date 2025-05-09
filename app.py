import streamlit as st
from ollama_client import query_ollama

st.set_page_config(page_title="Naive LLAMA Chatbot", page_icon="🤖")
st.title("🤖 Naive LLAMA Chatbot (Ollama)")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", "", key="user_input")
    submitted = st.form_submit_button("Send")

if submitted and user_input.strip():
    st.session_state.chat_history.append(("user", user_input))
    with st.spinner("LLAMA is thinking..."):
        response = query_ollama(user_input)
    st.session_state.chat_history.append(("bot", response))

for sender, msg in st.session_state.chat_history:
    if sender == "user":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**LLAMA:** {msg}")
