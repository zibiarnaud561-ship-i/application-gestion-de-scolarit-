import sqlite3

class Etudiant:
    def __init__(self, nom, prenom, matricule, filiere):
        self.nom = nom
        self.prenom = prenom
        self.matricule = matricule
        self.filiere = filiere

    def ajouter(self):
        conn = sqlite3.connect("db/scolarite.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO etudiants (nom, prenom, matricule, filiere)
            VALUES (?, ?, ?, ?)
        """, (self.nom, self.prenom, self.matricule, self.filiere))
        conn.commit()
        conn.close()

    @staticmethod
    def afficher_tous():
        conn = sqlite3.connect("db/scolarite.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM etudiants")
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def modifier(matricule, nouveau_nom, nouveau_prenom, nouvelle_filiere):
        conn = sqlite3.connect("db/scolarite.db")
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE etudiants
            SET nom=?, prenom=?, filiere=?
            WHERE matricule=?
        """, (nouveau_nom, nouveau_prenom, nouvelle_filiere, matricule))
        conn.commit()
        conn.close()

    @staticmethod
    def supprimer(matricule):
        conn = sqlite3.connect("db/scolarite.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM etudiants WHERE matricule=?", (matricule,))
        conn.commit()
        conn.close()
