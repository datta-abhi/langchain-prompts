from langchain_ollama.chat_models import ChatOllama
import streamlit as st

# instantiate model object
model = ChatOllama(model="llama3.2")

# streamlit ui
st.header("Menu Creation")
user_input = st.text_input("Enter your prompt:")

if st.button("Get help from LLM"):
    response = model.invoke(user_input)
    st.write(response.content)