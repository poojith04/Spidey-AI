from app.knowledge.document_loader import DocumentLoader
from app.knowledge.chunker import Chunker
from app.knowledge.embedder import Embedder
from app.knowledge.vector_store import VectorStore
from app.knowledge.retriever import Retriever
import os
from app.knowledge.knowledge_tracker import KnowledgeTracker

class KnowledgeEngine:

    def __init__(self):

        self.loader = DocumentLoader()

        self.chunker = Chunker()

        self.embedder = Embedder()

        self.store = VectorStore()

        self.tracker = KnowledgeTracker()

        self.retriever = Retriever(
            self.embedder,
            self.store
        )

        self.ready = False

    def index(self, folder):

        index_file = "storage/knowledge.index"
        metadata_file = "storage/knowledge.pkl"

        cache_exists = (
    os.path.exists(index_file)
    and os.path.exists(metadata_file)
        )

        knowledge_changed = self.tracker.has_changed(folder)

        if cache_exists and not knowledge_changed:

            self.store.load(
                index_file,
                metadata_file
            )

            self.ready = True

            print("⚡ Loaded cached knowledge index.")

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
        self.tracker.save_hash(
            self.tracker.generate_hash(folder)
        )

        self.ready = True

        print("✅ Knowledge Engine Ready!")
    
    def search(self, question, top_k=5):

        if not self.ready:
            return []

        return self.retriever.retrieve(
            question,
            top_k=top_k
        )

    def ask(self, question):

        return self.search(question)