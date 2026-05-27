import sqlite3

def initialiser_bd():
    conn = sqlite3.connect("scolarite.db")
    cursor = conn.cursor()

    # Table étudiants
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS etudiants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        prenom TEXT,
        matricule TEXT UNIQUE,
        filiere TEXT
    )
    """)

    # Table cours
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cours (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT UNIQUE,
        titre TEXT,
        credit INTEGER
    )
    """)

    # Table inscriptions
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inscriptions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        etudiant_id INTEGER,
        cours_id INTEGER,
        note REAL,
        FOREIGN KEY(etudiant_id) REFERENCES etudiants(id),
        FOREIGN KEY(cours_id) REFERENCES cours(id)
    )
    """)

    # Table users
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL CHECK(role IN ('admin','etudiant'))
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialiser_bd()
    print("✅ Base de données initialisée avec succès.")
