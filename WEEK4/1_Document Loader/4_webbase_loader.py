from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(
    template='Answer the following {Question} asked on the {text}',
    input_variables=['Question','text']
)

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
parser = StrOutputParser()

url = 'https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421'
loader = WebBaseLoader(url)

docs = loader.Load()
chain = prompt | model | parser

print(chain.invoke({'Question':'Which product we are talking about','text':docs[0].page_content}))
