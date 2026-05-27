import sqlite3

class Cours:
    def __init__(self, code, titre, credit):
        self.code = code
        self.titre = titre
        self.credit = credit

    # --- CREATE ---
    def ajouter(self):
        conn = sqlite3.connect("scolarite.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO cours (code, titre, credit)
            VALUES (?, ?, ?)
        """, (self.code, self.titre, self.credit))
        conn.commit()
        conn.close()

    # --- READ ---
    @staticmethod
    def afficher_tous():
        conn = sqlite3.connect("scolarite.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cours")
        rows = cursor.fetchall()
        conn.close()
        return rows

    # --- UPDATE ---
    @staticmethod
    def modifier(code, nouveau_titre, nouveau_credit):
        conn = sqlite3.connect("scolarite.db")
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE cours
            SET titre=?, credit=?
            WHERE code=?
        """, (nouveau_titre, nouveau_credit, code))
        conn.commit()
        conn.close()

    # --- DELETE ---
    @staticmethod
    def supprimer(code):
        conn = sqlite3.connect("scolarite.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cours WHERE code=?", (code,))
        conn.commit()
        conn.close()
