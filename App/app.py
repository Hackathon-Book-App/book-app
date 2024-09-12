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

#Creating RAG chain

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

#Getting user input and returning result

results = rag_chain.invoke({"input": "Who wrote atlas of middle earth?"})

print(results["answer"])

