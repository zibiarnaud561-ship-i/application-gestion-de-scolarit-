import os, sys
import sqlite3
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.etudiant import Etudiant
from src.cours import Cours
from src.inscription import Inscription
from src.bulletin import Bulletin

@pytest.fixture(autouse=True)
def setup_db():
    conn = sqlite3.connect("scolarite.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM inscriptions")
    cursor.execute("DELETE FROM etudiants")
    cursor.execute("DELETE FROM cours")
    conn.commit()
    conn.close()
    yield

def test_bulletin_moyenne_pdf():
    # Préparer données
    e = Etudiant("Durand", "Paul", "MAT002", "Maths")
    e.ajouter()
    c = Cours("PHY101", "Physique", 4)
    c.ajouter()

    # Récupérer IDs
    conn = sqlite3.connect("scolarite.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM etudiants WHERE matricule=?", ("MAT002",))
    etu_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM cours WHERE code=?", ("PHY101",))
    cours_id = cursor.fetchone()[0]
    conn.close()

    # Ajouter inscription
    i = Inscription(etu_id, cours_id, 14)
    i.ajouter()

    # Calculer moyenne
    moyenne = Bulletin.calculer_moyenne(etu_id)
    assert moyenne == 14

    # Générer PDF
    Bulletin.generer_pdf(etu_id, "bulletin_test.pdf")
    assert os.path.exists("bulletin_test.pdf")

    # Nettoyage
    os.remove("bulletin_test.pdf")
