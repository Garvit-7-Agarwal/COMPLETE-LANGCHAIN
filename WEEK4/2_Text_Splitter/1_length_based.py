from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader 

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_documents(docs)

print("\n\n\n\nHERE : ",result[1].page_content)
print(type(result))
print("\n\n",result)

