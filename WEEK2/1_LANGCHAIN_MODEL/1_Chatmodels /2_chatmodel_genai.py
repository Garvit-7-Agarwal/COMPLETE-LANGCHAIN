from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = 'gemini-2.5-flash',
    temperature=0.2,
    response_mime_type = "text/plain"
)

result = model.invoke("Who is Vaibhav Suryavanshi in cricket?")
print(result.content)