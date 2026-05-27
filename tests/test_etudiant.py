import os, sys
import sqlite3
import pytest

# Ajouter le chemin du projet
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.etudiant import Etudiant

@pytest.fixture(autouse=True)
def setup_db():
    conn = sqlite3.connect("scolarite.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM etudiants")
    conn.commit()
    conn.close()
    yield

def test_ajouter_etudiant():
    e = Etudiant("Mbarga", "Jean-Paul", "21TIC042", "TIC")
    e.ajouter()
    result = Etudiant.afficher_tous()
    assert len(result) == 1
    assert result[0][1] == "Mbarga"
    assert result[0][2] == "Jean-Paul"

def test_afficher_tous():
    e = Etudiant("Fotso", "Aminata", "21TIC057", "TIC")
    e.ajouter()
    result = Etudiant.afficher_tous()
    assert any(r[2] == "Aminata" for r in result)

def test_modifier_etudiant():
    e = Etudiant("Talla", "Eric", "21TIC112", "TIC")
    e.ajouter()
    Etudiant.modifier("21TIC112", "Talla", "Eric", "Informatique")
    result = Etudiant.afficher_tous()
    assert result[0][4] == "Informatique"

def test_supprimer_etudiant():
    e = Etudiant("Nguemo", "Sara", "21TIC099", "TIC")
    e.ajouter()
    Etudiant.supprimer("21TIC099")
    result = Etudiant.afficher_tous()
    assert len(result) == 0
