# It might be happen that we want to upload a folder which contains all the pdfs we want then this directory loader is used 
from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path='pdf_folder',
    glob='*.pdf', # This tells the DirectoryLoader which files to select. and * says that whatever the filename it should end with .pdf
    loader_cls=PyPDFLoader # This tells DirectoryLoader: # "Once you find the files, use PyPDFLoader to load each file."
)
# The DirectoryLoader internally uses this loader class to process each matching file.

docs = loader.lazy_load()
# The lazy_load can be useful when dealing with a large number of files, because you can process documents one at a time rather than immediately storing everything in memory.

for documents in docs:
    print(documents.metadata)