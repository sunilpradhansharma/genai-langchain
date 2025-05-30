from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

# Create a prompt using the template
prompt = chat_template.invoke({'domain':'Cloud Computing','topic':'Serverless Architecture'})

print(prompt)