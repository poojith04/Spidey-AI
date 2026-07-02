from app.knowledge.document_loader import DocumentLoader

loader = DocumentLoader()

docs = loader.load_folder("knowledge")

print("Documents found:", len(docs))

for doc in docs:
    print("=" * 40)
    print(doc["file"])
    print(doc["text"][:300])