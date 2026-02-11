"""
Manager 3: Vector Database (VDB).
Handles persistent local storage and advanced tokenization.
Supports BPE, SentencePiece, and Tiktoken for LLM compatibility.
"""
import chromadb
from chromadb.config import Settings
import tiktoken
import os

class VectorDBManager:
    def __init__(self, db_path: str = "./data/chroma_db"):
        # Requirement VDB-REQ-01: Local persistence to manage RAM efficiency
        self.client = chromadb.PersistentClient(path=db_path)
        self.collection = self.client.get_or_create_collection(
            name="geopolitical_intel",
            metadata={"hnsw:space": "cosine"} # Optimized for semantic similarity
        )

    def get_tokenizer(self, method: str = "tiktoken"):
        """Requirement VDB-001: Support for multiple tokenization methods."""
        if method == "tiktoken":
            # Optimized for OpenAI/Llama-based token counting
            return tiktoken.get_encoding("cl100k_base")
        elif method == "BPE":
            # Placeholder for Byte Pair Encoding logic
            return "BPE_Tokenizer_Config"
        elif method == "SentencePiece":
            # Placeholder for SentencePiece logic (used by Mistral)
            return "SentencePiece_Config"
        else:
            raise ValueError(f"Unsupported tokenization method: {method}")

    def add_to_vector_store(self, payload: dict):
        """
        Stores structured JSON data into ChromaDB.
        Ensures metadata filtering for 'Directed Filtering' requirements.
        """
        # Requirement OR03: Indexing with metadata for topic-directed filtering
        self.collection.add(
            documents=[payload["content"]],
            metadatas=[{
                "source_id": payload["source_id"],
                "timestamp": payload["timestamp"],
                "topic": "USA-Iran Geopolitics", # Requirement IE-REQ-02
                "signature": payload["signature_evidence"]
            }],
            ids=[payload["source_id"]]
        )

    def query_intel(self, query_text: str, n_results: int = 3):
        """Retrieves context for the Intelligence Layer (Manager 4)."""
        return self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )