from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

chat_history = []

while True:
    user_inpu = input("You : ")

    if(user_inpu == 'exit'): 
        break

    chat_history.append(user_inpu)
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI : ",result.content)
    
print(chat_history)

# now if we create large chat history the it might be possible that ai will not be possible to understand the human message and ai message