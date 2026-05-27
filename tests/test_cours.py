import os, sys
import sqlite3
import pytest

# Ajouter le chemin du projet
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.cours import Cours

@pytest.fixture(autouse=True)
def setup_db():
    conn = sqlite3.connect("scolarite.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cours")
    conn.commit()
    conn.close()
    yield

def test_ajouter_cours():
    c = Cours("MATH101", "Mathématiques", 5)
    c.ajouter()
    result = Cours.afficher_tous()
    assert len(result) == 1
    assert result[0][1] == "MATH101"          # code
    assert result[0][2] == "Mathématiques"    # titre
    assert result[0][3] == 5                  # credit

def test_modifier_cours():
    c = Cours("PHY101", "Physique", 4)
    c.ajouter()
    Cours.modifier("PHY101", "Physique Générale", 6)
    result = Cours.afficher_tous()
    assert result[0][2] == "Physique Générale"
    assert result[0][3] == 6

def test_supprimer_cours():
    c = Cours("CHM101", "Chimie", 3)
    c.ajouter()
    Cours.supprimer("CHM101")
    result = Cours.afficher_tous()
    assert len(result) == 0
