from cli_bookapp import Book

from dotenv import load_dotenv
load_dotenv(".venv/.env")

#Initiating client (the one on RPi)

import chromadb

client=chromadb.HttpClient(
    host="https://better-skink-promoted.ngrok-free.app",
    port=8000

)

#Instantiating vectorstore from DB and creating retriever

from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

vectorstore = Chroma(client=client, embedding_function=OpenAIEmbeddings())
retriever = vectorstore.as_retriever()

#Instantiating LLM

llm = ChatOpenAI(model="gpt-4o")

from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

#Creating prompt

system_prompt = (
    "You are an assistant for question-answering tasks. Use only the following pieces of retrieved context to answer the question.You are not allowed to use another source. If you don't know the answer, say that you don't know. Use three sentences maximum and keep the answer concise."
    "{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

#Creating RAG chain

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

#Getting user input and returning result

results = rag_chain.invoke({"input": f'Căuta cărți cu o parte din urmatoarele criterii genul: {Book.gen}, despre: {Book.topic}, stil: {Book.style}, în limba: {Book.language}, cu aproximativ {Book.pages} pagini.Tine cont ca nu trebuie sa indeplineasca exact criteriile.'})
#results = rag_chain.invoke({"input": f'Recommend 3 books about friendship.'})

print(results["answer"])
#print(results["context"])


