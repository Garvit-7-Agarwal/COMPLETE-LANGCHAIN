from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

chat_mess = []

chat_mess.append(SystemMessage(content="You are an helpful assistant"))
chat_mess.append(HumanMessage(content="Tell me about BBIS Sujangarh School"))

result = model.invoke(chat_mess)

chat_mess.append(AIMessage(content=result.content))

print(chat_mess)