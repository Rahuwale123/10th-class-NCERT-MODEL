from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from app.config import (
    QDRANT_URL, COLLECTION_NAME,
    EMBEDDING_MODEL
)

class VectorService:
    def __init__(self):
        # Initialize Qdrant client with the hosted instance URL
        self.client = QdrantClient(
            url=QDRANT_URL,
            timeout=300,  # 5 minutes timeout
            prefer_grpc=False  # Use HTTP instead of gRPC for better compatibility
        )
        self.embedding_model = SentenceTransformer(EMBEDDING_MODEL)

    def search(self, query: str, limit: int = 7) -> list:
        """
        Search for relevant context using vector similarity
        """
        query_vector = self.embedding_model.encode(query).tolist()
        results = self.client.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_vector,
            limit=limit,
            score_threshold=0.3,  # Lowered threshold to get more results
            with_payload=True,
            with_vectors=False
        )
        
        # Debug: Print search results
        print(f"\nSearch Results for query: {query}")
        for i, r in enumerate(results):
            print(f"\nResult {i+1}:")
            print(f"Score: {r.score}")
            print(f"Source: {r.payload.get('source', 'N/A')}")
            print(f"Text preview: {r.payload.get('text', '')[:200]}...")
        
        return [r.payload.get("text", "") for r in results if r.payload.get("text")]

    def get_context(self, query: str) -> str:
        """
        Get formatted context from vector search
        """
        context_chunks = self.search(query)
        if not context_chunks:
            return "No relevant context found."
        return "\n---\n".join(context_chunks) 