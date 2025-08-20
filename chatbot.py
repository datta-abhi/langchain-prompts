from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# instantiate model
model = ChatOllama(model="llama3.2")

system_msg = SystemMessage("You are a helpful assistant who gives concise answers.")
chat_history = [system_msg]

while True:
    user_input = input("You: \n")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    response = model.invoke(chat_history)
    print("AI:\n", response.content)
    chat_history.append(AIMessage(content=response.content))
    
print(chat_history)  