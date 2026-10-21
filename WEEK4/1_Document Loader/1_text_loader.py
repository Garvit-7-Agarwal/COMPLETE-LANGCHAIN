from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate 
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
parser = StrOutputParser()

prompt = PromptTemplate(
    template='Write a summary on the following poem -> {poem}',
    input_variables=['poem']
)

loader = TextLoader('cricket.txt',encoding='utf-8')
documents = loader.load()
# text loader returns the list and each element contains page content and meta data 

print("Length : ",len(documents))
print("Type : ",type(documents))
print(documents[0].page_content)
print(documents[0].metadata)

chain = prompt|model|parser

print("\n")
print("Chain result : ",chain.invoke({'poem':documents[0].page_content}))