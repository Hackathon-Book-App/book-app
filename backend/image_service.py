def image_service(path):
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()
    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print(f"Texts: ")

    image_input=[]
    for text in texts:
        image_input.append(text.description)

    image_input.pop(0)

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )
    
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
    retriever = vectorstore.as_retriever(k=500)

    #Instantiating LLM

    llm = ChatOpenAI(model="gpt-4o")


    from langchain_core.prompts import ChatPromptTemplate
    from langchain.chains.combine_documents import create_stuff_documents_chain
    from langchain.chains import create_retrieval_chain

    #Creating prompt

    system_prompt = (     
        "You will be provided with a set of documents." 
        "Your task is to recommend 2 books using only the provided documents and the user input."
        "If the documents do not contain the information needed then simply write:"
        "'Insufficient information.'"
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
    user_input=image_input
    
    #results = rag_chain.invoke({"input": f'Căuta cărți cu o parte din urmatoarele criterii genul: {book_object.gen}, despre: {book_object.topic}, stil: {book_object.style}, în limba: {book_object.language}, cu aproximativ {book_object.pages} pagini. Tine cont ca nu trebuie sa indeplineasca exact criteriile.'})
    results = rag_chain.invoke({"input": user_input})

    
    

    return results