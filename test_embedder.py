from app.knowledge.document_loader import DocumentLoader
from app.knowledge.chunker import Chunker
from app.knowledge.embedder import Embedder

loader = DocumentLoader()
chunker = Chunker()
embedder = Embedder()

documents = loader.load_folder("knowledge")

chunks = []

for doc in documents:
    chunks.extend(
        chunker.split(doc["text"])
    )

embeddings = embedder.embed(chunks)

print()

print("Chunks:", len(chunks))
print("Embeddings:", len(embeddings))

print()

print("Embedding Dimension:", len(embeddings[0]))