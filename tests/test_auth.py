import os, sys
import sqlite3
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.auth import Auth

@pytest.fixture(autouse=True)
def setup_db():
    conn = sqlite3.connect("scolarite.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users")
    conn.commit()
    conn.close()
    yield

def test_register_and_login_admin():
    a = Auth("admin1", "1234", "admin")
    a.register()
    result = Auth.login("admin1", "1234")
    assert "admin" in result

def test_register_and_login_etudiant():
    e = Auth("etu1", "abcd", "etudiant")
    e.register()
    result = Auth.login("etu1", "abcd")
    assert "etudiant" in result

def test_login_fail():
    result = Auth.login("unknown", "wrong")
    assert "Échec" in result
