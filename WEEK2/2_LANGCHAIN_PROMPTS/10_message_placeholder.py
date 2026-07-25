# A Message placeholder in Langchain is a special placeholder used inside a ChatpromptTemplate to dynamically insert Chat history or a list of messages at run time 

from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

template = ChatPromptTemplate([
    ('system','you are an helpful Customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []
with open('11_chat_history.txt') as f:
    chat_history.extend(f.readlines())

prompt = template.invoke({'chat_history':chat_history,'query':"What about my refund"})

result = model.invoke(prompt)
print(result.content)