from langchain_community.document_loaders import TextLoader 
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAI

# Load the document 
loader = TextLoader('cricket.txt') # here the text loader only reads text file not pdf , for pdf use pypdf loader
documents = loader.load()

# split the text into smaller chunks 
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# convert text into embeddings & store in FAISS
vectorstore = FAISS.from_documents(docs,GoogleGenerativeAIEmbeddings())

# Crete a retriver (fetches relevant documents )
retriever = vectorstore.as_retriever()

# Manually Retirive relevant documents 
