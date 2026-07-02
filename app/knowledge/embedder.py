from sentence_transformers import SentenceTransformer


class Embedder:

    def __init__(self):

        print("🧠 Loading embedding model...")

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        print("✅ Embedding model loaded.")

    def embed(self, chunks):

        return self.model.encode(
            chunks,
            convert_to_numpy=True
        )