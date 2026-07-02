from app.knowledge.document_loader import DocumentLoader
from app.knowledge.chunker import Chunker

loader = DocumentLoader()
chunker = Chunker()

documents = loader.load_folder("knowledge")

for doc in documents:

    print("=" * 60)
    print(doc["file"])

    chunks = chunker.split(doc["text"])

    print(f"Chunks: {len(chunks)}")
    print()
    print(chunks[0])