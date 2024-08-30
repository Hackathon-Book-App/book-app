from langchain_community.document_loaders import PyPDFDirectoryLoader

directory_path = "C:\\Users\\raoul\\source\\Myprojects\\Hackathon\\TheBooks\\Pdf Books"
loader = PyPDFDirectoryLoader(directory_path)

docs = loader.load()

print(len(docs))

import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()



from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings(), persist_directory=".\\embeddedBookDB")