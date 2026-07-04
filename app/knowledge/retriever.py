class Retriever:

    def __init__(self, embedder, vector_store):

        self.embedder = embedder
        self.vector_store = vector_store

    def retrieve(self, question, top_k=5):

        embedding = self.embedder.embed(
            [question]
        )[0]

        return self.vector_store.search(
            embedding,
            top_k=top_k
        )