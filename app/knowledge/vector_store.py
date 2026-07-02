import faiss
import numpy as np
import os
import pickle


class VectorStore:

    def __init__(self):

        self.index = None
        self.records = []

    def build(self, embeddings, records):

        embeddings = np.asarray(
            embeddings,
            dtype="float32"
        )

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.index.add(embeddings)

        self.records = records

    def search(self, query_embedding, top_k=5):

        query_embedding = np.asarray(
            [query_embedding],
            dtype="float32"
        )

        _, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for idx in indices[0]:

            if idx != -1:
                results.append(
                    self.records[idx]
                )

        return results
    def save(self,
         index_path="storage/knowledge.index",
         metadata_path="storage/knowledge.pkl"):

        os.makedirs("storage", exist_ok=True)

        faiss.write_index(self.index, index_path)

        with open(metadata_path, "wb") as file:
            pickle.dump(self.records, file)

        print("💾 Knowledge index saved.")
    def load(self,
         index_path="storage/knowledge.index",
         metadata_path="storage/knowledge.pkl"):

        self.index = faiss.read_index(index_path)

        with open(metadata_path, "rb") as file:
            self.records = pickle.load(file)
