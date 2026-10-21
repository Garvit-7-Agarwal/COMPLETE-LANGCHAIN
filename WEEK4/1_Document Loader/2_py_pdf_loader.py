from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Networking Basics.pdf')

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)

# this pypdf loader is good until the pdf document contains text messages if the document contains more images or more tables then there are some other loaders fot that we can prepfer them (see notes)

# Py pdf split each page of the document , if the pdf document contains 20 pages then pypdf will split the documents into 20 parts each part is the page of the documents 