from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

chat_message = []
chat_message.append(SystemMessage(content='You are and helpful assistant.'))

while True:
    user_input = input("You : ")
    if(user_input == 'exit'):
        break
    chat_message.append(HumanMessage(content=user_input))
    result = model.invoke(user_input)
    chat_message.append(AIMessage(content=result.content))
    print("AI : ",result.content)

print(chat_message)

