import sqlite3
import os
from recognizer import FaceRecognizer


def delete_person(name):

    conn = sqlite3.connect("database/faces.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT image_path FROM persons WHERE name=?",
        (name,)
    )

    result = cursor.fetchone()

    if result is None:
        conn.close()
        return False

    image_path = result[0]

    if os.path.exists(image_path):
        os.remove(image_path)

    cursor.execute(
        "DELETE FROM persons WHERE name=?",
        (name,)
    )

    conn.commit()
    conn.close()

    recognizer = FaceRecognizer()
    recognizer.create_encodings()

    return True