from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import ChatOllama

# instantiate model
model = ChatOllama(model="llama3.2")

# sample new query
new_query = "how much refund will I receive?"

# chat template
template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent who gives short but accurate replies.'),
    MessagesPlaceholder(variable_name= 'chat_history'),
    ('human','{new_query}')
])

# loading chat_history
chat_history = []
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())
    
# print(chat_history) 

# # invoking prompt
# prompt = template.invoke({'chat_history': chat_history,
#                           'new_query':new_query})

# print(prompt)

# invoking model using chains
chain = template | model
response = chain.invoke({'chat_history': chat_history,
                          'new_query':new_query})

print(response.content)