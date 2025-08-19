import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

# instantiate model
model = ChatOllama(model="llama3.2")

# Streamlit UI
st.header("Restaurant Menu Ideate")

# get cusine option from user
cuisine = st.selectbox("Select cuisine type",["Indian","Chinese","Italian"])

# get nos of items from user
nos_items = st.number_input("Select nos of items",min_value=2, max_value=15, value=5, step=1)

# get veg/ non-veg options from user
dietary = st.selectbox("Select veg/ non-veg or both",["veg","non-veg","veg and non-veg"])

user_prompt = PromptTemplate.from_template("""
                                      Create a {cuisine} restaurant menu containing {nos_items} items.
                                      It should have {dietary} options only.
                                      Give only the names of dishes as numbered list.
                                      """)

# if st.button("Create menu"):
#     # formatted prompt with user inputs in placeholders
#     formatted_prompt = user_prompt.format(cuisine = cuisine, nos_items = nos_items, dietary = dietary) 
    
#     response = model.invoke(formatted_prompt)
#     st.write(response.content)

# alternate using chain
chain = user_prompt | model
if st.button("Create menu"):
    # formatted prompt with user inputs in placeholders
    
    response = chain.invoke({"cuisine": cuisine, "nos_items": nos_items,"dietary": dietary})
    st.write(response.content)