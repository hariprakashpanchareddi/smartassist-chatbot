import chromadb
from chromadb.api.types import Documents, EmbeddingFunction, Embeddings
from sentence_transformers import SentenceTransformer
import os

class MiniLMEmbeddingFunction(EmbeddingFunction):
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
    
    def __call__(self, input: Documents) -> Embeddings:
        embeddings = self.model.encode(input)
        return embeddings.tolist()

db_path = os.path.join(os.getcwd(), 'data', 'chroma_db')
chroma_client = chromadb.PersistentClient(path=db_path)
embedding_fn = MiniLMEmbeddingFunction()
collection = chroma_client.get_or_create_collection(
    name="smartassist_kb",
    embedding_function=embedding_fn
)
