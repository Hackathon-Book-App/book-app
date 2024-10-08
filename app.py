def App(book_object):
    # from dotenv import load_dotenv
    # load_dotenv(".venv/.env")

    #Initiating client (the one on RPi)

    import chromadb

    client=chromadb.HttpClient(
        host="https://widely-proven-bobcat.ngrok-free.app",
        port=8000

    )

    #Instantiating vectorstore from DB and creating retriever

    from langchain_chroma import Chroma
    from langchain_openai import ChatOpenAI, OpenAIEmbeddings

    vectorstore = Chroma(client=client, embedding_function=OpenAIEmbeddings())
    retriever = vectorstore.as_retriever(search_type='mmr',k=10)

    #Instantiating LLM

    llm = ChatOpenAI(model="gpt-4o")

    from langchain_core.prompts import ChatPromptTemplate
    from langchain.chains.combine_documents import create_stuff_documents_chain
    from langchain.chains import create_retrieval_chain

    #Creating prompt

    system_prompt = (
        # """You are an assistant for recommending books based on an user input.
        # Use only the following pieces of information to recommend books.
        # If the answer is not in the provided information, say you don't know."""
        "You will be provided with a set of documents." 
        "Your task is to answer the question using only the provided documents and" 
        "to cite the passage(s) of the document used to answer the question."
        "If the documents do not contain the information needed to answer the question"
        "then simply write: 'Insufficient information.' If an answer to the question is provided," 
        'it must be annotated with a citation.'
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
    user_input=f'''Recommend 2 books with the following properties, in this order of importance: 
    1. topic: {book_object.topic},
    2. language: {book_object.language},
    3. writing style: {book_object.style},
    4. maximum pages: {book_object.max_pages},
    5. minimum pages: {book_object.min_pages}.''' 
    
    #results = rag_chain.invoke({"input": f'Căuta cărți cu o parte din urmatoarele criterii genul: {book_object.gen}, despre: {book_object.topic}, stil: {book_object.style}, în limba: {book_object.language}, cu aproximativ {book_object.pages} pagini. Tine cont ca nu trebuie sa indeplineasca exact criteriile.'})
    results = rag_chain.invoke({"input": user_input})
    return results