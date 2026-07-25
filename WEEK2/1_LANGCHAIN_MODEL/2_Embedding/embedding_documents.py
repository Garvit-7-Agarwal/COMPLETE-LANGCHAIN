from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

documnets = [
    "Jaipur is the pink city",
    "Delhi is the capital of india",
    "kolkata is capital city of west bengal",
    "taj mahal is located at agra",
    "manali is in himachal pradesh"
]

embed_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
result = embed_model.embed_documents(documnets)

print(str(result))