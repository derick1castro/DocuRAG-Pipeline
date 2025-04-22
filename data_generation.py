from config import settings
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

# Data Generation
# ----------------
# Responsible for constructing the RAG chain and formatting the prompt.


def build_rag_chain(retriever):
    """
    Build and return a Retrieval-Augmented Generation chain.
    """
    template = """
    You are an assistant for question-answering tasks.
    Use the following pieces of retrieved context to answer the question.
    If you don't know the answer, just say that you don't know.
    Use ten sentences maximum and keep the answer concise.

    Question: {question}
    Context: {context}

    Answer:
    """
    prompt = ChatPromptTemplate.from_template(template)

    llm = ChatOpenAI(
        openai_api_key=settings.OPENAI_API_KEY,
        model_name=settings.MODEL
    )
    output_parser = StrOutputParser()

    # Chain: retrieve -> prompt -> LLM -> parse
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}  
        | prompt  
        | llm  
        | output_parser
    )
    return rag_chain