from app.knowledge.document_loader import DocumentLoader
from app.knowledge.chunker import Chunker
from app.knowledge.embedder import Embedder
from app.knowledge.vector_store import VectorStore
from app.knowledge.retriever import Retriever

loader = DocumentLoader()
chunker = Chunker()
embedder = Embedder()
store = VectorStore()

documents = loader.load_folder("knowledge")

chunks = []

for doc in documents:

    chunks.extend(
        chunker.split(doc["text"])
    )

embeddings = embedder.embed(chunks)

store.build(
    embeddings,
    chunks
)

retriever = Retriever(
    embedder,
    store
)

results = retriever.retrieve(
    "What is Transfer Learning?"
)

print()

print("="*60)

for i, chunk in enumerate(results, 1):

    print(f"Result {i}")

    print("-"*60)

    print(chunk)

    print()