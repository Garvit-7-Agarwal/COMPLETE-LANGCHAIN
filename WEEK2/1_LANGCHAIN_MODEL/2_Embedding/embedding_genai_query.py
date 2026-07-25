from dotenv import load_dotenv
import os 
import getpass
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv() 
# The code load_dotenv loads the api key from the .env file to the variable os.environ["GOOGLE_API_KEY"]

api_key = os.getenv("GOOGLE_API_KEY")
if not os.environ.get("GOOGLE_API_KEY"):
    api_key = os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key of Gemini : ")
if not api_key:
    raise ValueError("❌ GOOGLE_API_KEY not found. Please set it in your .env file.")

embed = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
vector = embed.embed_query("hello,world!")

print("Vector length : ",len(vector))
print("First 50 values : ",vector[:50])
