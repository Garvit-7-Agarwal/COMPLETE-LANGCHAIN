from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system','You are an helpful assitant in the domain of {domain}'),
    ('human','What do you mean by {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Long off'})
print(prompt)