from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

# instantiate model
model = ChatOllama(model="llama3.2")

# create dynamic prompt using ChatPromptTemplate
template = ChatPromptTemplate([
    ('system','You are an expert in {domain} who gives concise but accurate answers.'),
    ('human','Explain about {topic}')
])

# create chain
chain = template | model
response = chain.invoke({'domain':'clinical medicine',
                          'topic': 'offside'})
print(response.content)