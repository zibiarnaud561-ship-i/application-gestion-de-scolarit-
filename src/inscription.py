import sqlite3

class Inscription:
    def __init__(self, etudiant_id, cours_id, note=None):
        self.etudiant_id = etudiant_id
        self.cours_id = cours_id
        self.note = note

    # --- CREATE ---
    def ajouter(self):
        conn = sqlite3.connect("scolarite.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO inscriptions (etudiant_id, cours_id, note)
            VALUES (?, ?, ?)
        """, (self.etudiant_id, self.cours_id, self.note))
        conn.commit()
        conn.close()

    # --- READ ---
    @staticmethod
    def afficher_toutes():
        conn = sqlite3.connect("scolarite.db")
        cursor = conn.cursor()
        # Version simple : on renvoie directement les colonnes de la table
        cursor.execute("SELECT id, etudiant_id, cours_id, note FROM inscriptions")
        rows = cursor.fetchall()
        conn.close()
        return rows

    # --- UPDATE ---
    @staticmethod
    def modifier(inscription_id, nouvelle_note):
        conn = sqlite3.connect("scolarite.db")
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE inscriptions
            SET note=?
            WHERE id=?
        """, (nouvelle_note, inscription_id))
        conn.commit()
        conn.close()

    # --- DELETE ---
    @staticmethod
    def supprimer(inscription_id):
        conn = sqlite3.connect("scolarite.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM inscriptions WHERE id=?", (inscription_id,))
        conn.commit()
        conn.close()
