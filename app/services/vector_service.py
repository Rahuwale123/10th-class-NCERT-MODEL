from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from app.config import (
    QDRANT_HOST, QDRANT_PORT, COLLECTION_NAME,
    EMBEDDING_MODEL
)

class VectorService:
    def __init__(self):
        self.client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)
        self.embedding_model = SentenceTransformer(EMBEDDING_MODEL)

    def search(self, query: str, limit: int = 7) -> list:
        """
        Search for relevant context using vector similarity
        """
        query_vector = self.embedding_model.encode(query).tolist()
        results = self.client.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_vector,
            limit=limit
        )
        return [r.payload.get("text", "") for r in results if r.payload.get("text")]

    def get_context(self, query: str) -> str:
        """
        Get formatted context from vector search
        """
        context_chunks = self.search(query)
        return "\n---\n".join(context_chunks) 