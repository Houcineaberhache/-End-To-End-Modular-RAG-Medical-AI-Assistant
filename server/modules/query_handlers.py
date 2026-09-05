from logger import logger

def query_chain(chain, user_input: str):
    try:
        logger.debug(f"Running chain for input: {user_input}")
        result = chain.invoke(user_input)
        response = {
            "response": result["result"],
            "sources": [
                f"{doc.metadata.get('source', 'unknown')} (page {doc.metadata.get('page', '?')})"
                for doc in result["source_documents"]
            ]
        }
        logger.debug(f"Chain response:{response}")
        return response
    except Exception as e:
        logger.exception("Error on query chain")
        raise