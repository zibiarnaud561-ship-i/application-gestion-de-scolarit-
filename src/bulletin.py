import sqlite3
from fpdf import FPDF   # pour export PDF

class Bulletin:
    def __init__(self, etudiant_id):
        self.etudiant_id = etudiant_id

    def calculer_moyenne(self):
        conn = sqlite3.connect("scolarite.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT AVG(note)
            FROM inscriptions
            WHERE etudiant_id=? AND note IS NOT NULL
        """, (self.etudiant_id,))
        moyenne = cursor.fetchone()[0]
        conn.close()
        return round(moyenne, 2) if moyenne else 0

    def mention(self, moyenne):
        if moyenne >= 16:
            return "Très Bien"
        elif moyenne >= 14:
            return "Bien"
        elif moyenne >= 12:
            return "Assez Bien"
        elif moyenne >= 10:
            return "Passable"
        else:
            return "Échec"

    def generer_bulletin(self):
        conn = sqlite3.connect("scolarite.db")
        cursor = conn.cursor()

        # Récupérer infos étudiant
        cursor.execute("SELECT nom, prenom, matricule, filiere FROM etudiants WHERE id=?", (self.etudiant_id,))
        etudiant = cursor.fetchone()

        # Récupérer notes
        cursor.execute("""
            SELECT c.titre, i.note, c.credit
            FROM inscriptions i
            JOIN cours c ON i.cours_id = c.id
            WHERE i.etudiant_id=?
        """, (self.etudiant_id,))
        notes = cursor.fetchall()
        conn.close()

        moyenne = self.calculer_moyenne()
        mention = self.mention(moyenne)

        # --- Génération PDF ---
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, f"Bulletin de {etudiant[1]} {etudiant[0]}", ln=True, align="C")
        pdf.cell(200, 10, f"Matricule : {etudiant[2]} | Filière : {etudiant[3]}", ln=True, align="C")
        pdf.ln(10)

        for titre, note, credit in notes:
            pdf.cell(200, 10, f"{titre:<30} {note if note else 'N/A'} /20 | Crédit : {credit}", ln=True)

        pdf.ln(10)
        pdf.cell(200, 10, f"Moyenne : {moyenne}/20 | Mention : {mention}", ln=True)

        pdf.output(f"bulletin_{etudiant[2]}.pdf")
        print(f"Bulletin généré : bulletin_{etudiant[2]}.pdf")
