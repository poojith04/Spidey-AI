import sqlite3


class SQLiteMemory:

    def __init__(self):

        self.connection = sqlite3.connect(
            "spidey.db",
            check_same_thread=False
        )

        self.cursor = self.connection.cursor()

        self.create_table()

    def create_table(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            key TEXT UNIQUE,

            value TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """)

        self.connection.commit()

    def remember(self, key, value):

        self.cursor.execute("""

        INSERT INTO memories(key,value)

        VALUES(?,?)

        ON CONFLICT(key)

        DO UPDATE SET

        value=excluded.value

        """, (key, value))

        self.connection.commit()

    def recall(self, key):

        self.cursor.execute(

            "SELECT value FROM memories WHERE key=?",

            (key,)

        )

        result = self.cursor.fetchone()

        if result:

            return result[0]

        return None
