from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

documnets = [
    "Jaipur is the pink city",
    "Delhi is the capital of india",
    "kolkata is capital city of west bengal",
    "taj mahal is located at agra",
    "manali is in himachal pradesh"
]

query = "Where is located?"

embed_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

embed_documents = embed_model.embed_documents(documnets)
embed_query = embed_model.embed_query(query)

# now in cosine_similarity function we need to pass the embedding in the list 

result = cosine_similarity([embed_query],embed_documents)[0] # Jo result ayega vo 2D list ayega par hame simple list chaiye 2D list nahi chaiye to ham [0] laga denge so 2D list na aye

print(list(enumerate(result)))
print("\n")
print(sorted(list(enumerate(result)),key = lambda x:x[1]))
print("\n")
index,score = sorted(list(enumerate(result)),key = lambda x:x[1])[-1]

print(query)
print(documnets[index])
print("Score : ",score)