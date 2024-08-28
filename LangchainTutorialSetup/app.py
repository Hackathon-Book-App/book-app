from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import UnstructuredEPubLoader

file_path = "C:\\Users\\raoul\\source\\Myprojects\\Hackathon\\TheBooks\\BookShare\\1984 - George Orwell.epub"
loader = UnstructuredEPubLoader("C:\\Users\\raoul\\source\\Myprojects\\Hackathon\\TheBooks\\BookShare\\1984 - George Orwell.epub", mode="elements")

docs = loader.load()

# UnstructuredEPubLoader returns metadata as list, Chroma works with strings
#Try filtering complex metadata from the document using langchain_community.vectorstores.utils.filter_complex_metadata.

import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o")

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())

retriever = vectorstore.as_retriever()

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)


question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

results = rag_chain.invoke({"input": "Who wrote 1984?"})

results

# print(results["context"][0].page_content)
# print(results["context"][0].metadata)