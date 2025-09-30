from pydoc import doc
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("D:\Docs\COMPUTER_GRADE-I-COMPUTER-MID TERM EXAM REVISION-25-26-QP-PAN INDIA_Assignment.pdf")
documents = loader.load()
print("Testing PDF Loader")
print(f"Loaded {len(documents)} documents") 

#print(documents[0].page_content)
print(documents[0].metadata)