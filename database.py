import sqlite3


class DatabaseManager:

    def __init__(self):
        self.connection = sqlite3.connect("database/faces.db")
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS persons(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            image_path TEXT NOT NULL
        )
        """)
        self.connection.commit()

    def insert_person(self, name, image_path):
        self.cursor.execute(
            "INSERT INTO persons(name, image_path) VALUES(?, ?)",
            (name, image_path)
        )
        self.connection.commit()

    def close(self):
        self.connection.close()