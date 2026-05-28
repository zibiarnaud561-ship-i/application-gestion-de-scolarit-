import sqlite3


class Cours:

    def __init__(self, code, titre, credit):

        self.code = code

        self.titre = titre

        self.credit = credit


    def ajouter(self):

        conn = sqlite3.connect("db/scolarite.db")

        cursor = conn.cursor()

        cursor.execute("""

            INSERT INTO cours
            (code, titre, credit)

            VALUES (?, ?, ?)

        """, (

            self.code,
            self.titre,
            self.credit
        ))

        conn.commit()

        conn.close()

        print("✅ Cours ajouté.")