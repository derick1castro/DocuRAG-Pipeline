from data_ingestion import ingest_data
from data_retrieval import build_retriever
from data_generation import build_rag_chain
from loguru import logger

if __name__ == "__main__":

    # 1) Ingest
    try:
        logger.info("Application started")

        # 1) Ingest
        docs = ingest_data("./data/state_of_the_union.txt")
        logger.info("Data ingestion completed successfully")

        # 2) Retrieve
        retriever = build_retriever(docs)
        logger.info("Data retrieval completed successfully")

        # 3) Generate chain
        rag_chain = build_rag_chain(retriever)
        logger.info("RAG chain constructed successfully")

        # 4) Handle user query
        question = input("Write your question: ")
        logger.info(f"Received question: {question}")
        response = rag_chain.invoke(question)
        logger.info("Generated response successfully")

        print(f"\nResponse:\n{response}")
    except Exception as e:
        logger.error(f"Pipeline failed: {e}", exc_info=True)
        print("An error occurred. Check logs for details.")