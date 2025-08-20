from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# instantiate model
model = ChatOllama(model="llama3.2")

system_msg = SystemMessage("You are a helpful assistant")
user_msg = HumanMessage("Tell me about Virat Kohli")

messages = [system_msg,user_msg]

response = model.invoke(messages)
messages.append(AIMessage(content=response.content))
print(response.content)
print('--'*30)
print(messages)