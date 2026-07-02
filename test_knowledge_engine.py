from app.knowledge.knowledge_engine import KnowledgeEngine

engine = KnowledgeEngine()

engine.index("knowledge")

print()

results = engine.ask(
    "What is Transfer Learning?"
)

for i, result in enumerate(results, 1):

    print("=" * 60)

    print("Source :", result["source"])

    print("Chunk  :", result["chunk_id"])

    print()

    print(result["text"])