import hashlib
from pathlib import Path


class KnowledgeTracker:

    def __init__(self):

        self.hash_file = "storage/knowledge.hash"

    def generate_hash(self, folder):

        folder = Path(folder)

        sha = hashlib.sha256()

        files = sorted(folder.iterdir())

        for file in files:

            if file.is_file():

                sha.update(file.name.encode())

                sha.update(
                    str(file.stat().st_mtime).encode()
                )

                sha.update(
                    str(file.stat().st_size).encode()
                )

        return sha.hexdigest()

    def save_hash(self, value):

        with open(self.hash_file, "w") as file:
            file.write(value)

    def load_hash(self):

        try:

            with open(self.hash_file) as file:
                return file.read().strip()

        except FileNotFoundError:

            return None

    def has_changed(self, folder):

        current = self.generate_hash(folder)

        previous = self.load_hash()

        return current != previous