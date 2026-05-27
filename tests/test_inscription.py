import os, sys
import sqlite3
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.etudiant import Etudiant
from src.cours import Cours
from src.inscription import Inscription

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

def test_ajouter_inscription():
    e = Etudiant("Dupont", "Jean", "MAT001", "Informatique")
    e.ajouter()
    c = Cours("MATH101", "Mathématiques", 5)
    c.ajouter()

    conn = sqlite3.connect("scolarite.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM etudiants WHERE matricule=?", ("MAT001",))
    etu_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM cours WHERE code=?", ("MATH101",))
    cours_id = cursor.fetchone()[0]
    conn.close()

    i = Inscription(etu_id, cours_id, 15)
    i.ajouter()
    result = Inscription.afficher_toutes()
    assert len(result) == 1
    assert result[0][3] == 15  # note

def test_modifier_supprimer_inscription():
    e = Etudiant("Mbarga", "Luc", "MAT003", "Info")
    e.ajouter()
    c = Cours("CHM101", "Chimie", 3)
    c.ajouter()

    conn = sqlite3.connect("scolarite.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM etudiants WHERE matricule=?", ("MAT003",))
    etu_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM cours WHERE code=?", ("CHM101",))
    cours_id = cursor.fetchone()[0]
    conn.close()

    i = Inscription(etu_id, cours_id, 12)
    i.ajouter()
    result = Inscription.afficher_toutes()
    insc_id = result[0][0]

    # Modifier
    Inscription.modifier(insc_id, 16)
    result = Inscription.afficher_toutes()
    assert result[0][3] == 16

    # Supprimer
    Inscription.supprimer(insc_id)
    result = Inscription.afficher_toutes()
    assert len(result) == 0
