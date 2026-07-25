from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

while(1):
    user_inp = input("You : ")
    if user_inp == "exit":
        break
    result = model.invoke(user_inp)
    print("AI : ",result.content)

# Now there is a problem that the chatbot do not remember the past conservataion or past chat history so we will create a list of chat history which will store the chats 