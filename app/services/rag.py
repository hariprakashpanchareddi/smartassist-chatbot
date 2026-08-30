from app.services.vector_store import collection

def retrieve_context(query: str, top_k: int = 3) -> list[dict]:
    """
    Retrieves the top-K most relevant documents from the knowledge base.
    Returns a list of dictionaries with content, metadata, and distance.
    """
    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )

    retrieved_docs = []
    # ChromaDB returns nested lists (one list per query)
    if results and results.get('documents') and len(results['documents'][0]) > 0:
        for i in range(len(results['documents'][0])):
            doc = {
                "id": results['ids'][0][i],
                "content": results['documents'][0][i],
                "metadata": results['metadatas'][0][i],
                "distance": results['distances'][0][i]
            }
            retrieved_docs.append(doc)
            
    return retrieved_docs
