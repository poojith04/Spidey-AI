from app.knowledge.document_loader import DocumentLoader
from app.knowledge.chunker import Chunker
from app.knowledge.embedder import Embedder
from app.knowledge.vector_store import VectorStore
from app.knowledge.retriever import Retriever
import os

class KnowledgeEngine:

    def __init__(self):

        self.loader = DocumentLoader()
        self.chunker = Chunker()
        self.embedder = Embedder()
        self.store = VectorStore()

        self.retriever = Retriever(
            self.embedder,
            self.store
        )

        self.ready = False

    def index(self, folder):

        index_file = "storage/knowledge.index"
        metadata_file = "storage/knowledge.pkl"

        if os.path.exists(index_file) and os.path.exists(metadata_file):

            self.store.load(
                index_file,
                metadata_file
            )

            self.ready = True

            print("📚 Cached Knowledge Loaded!")

            return

        print("📚 Building Knowledge Base...")

        documents = self.loader.load_folder(folder)

        chunk_records = []

        for doc in documents:

            chunks = self.chunker.split(doc["text"])

            for index, chunk in enumerate(chunks):

                chunk_records.append({
                    "text": chunk,
                    "source": doc["file"],
                    "chunk_id": index
                })

        print(f"📄 Documents: {len(documents)}")
        print(f"🧩 Chunks: {len(chunk_records)}")

        embeddings = self.embedder.embed(
            [record["text"] for record in chunk_records]
        )

        self.store.build(
            embeddings,
            chunk_records
        )

        self.store.save(
            index_file,
            metadata_file
        )

        self.ready = True

        print("✅ Knowledge Engine Ready!")