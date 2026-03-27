import faiss
import pickle
from sentence_transformers import SentenceTransformer


class VisaSemanticSearch:

    def __init__(self):
        print("Loading embedding model...")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        print("Loading FAISS index...")
        self.index = faiss.read_index("vector_store/visa.index")

        print("Loading metadata...")
        with open("vector_store/metadata.pkl", "rb") as f:
            self.data = pickle.load(f)

        print("Semantic search ready.\n")

    def search(self, query, top_k=5):
        """
        Pure semantic retrieval.
        No rule-based filtering.
        """

        query_vector = self.model.encode([query])
        distances, indices = self.index.search(query_vector, top_k)

        results = []
        for idx in indices[0]:
            results.append(self.data[idx]["text"])

        return results