import sqlite3


def initialiser_bd():

    conn = sqlite3.connect(
        "db/scolarite.db"
    )

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

            FOREIGN KEY(etudiant_id)
            REFERENCES etudiants(id),

            FOREIGN KEY(cours_id)
            REFERENCES cours(id)
        )

    """)

    # Table utilisateurs
    cursor.execute("""

        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT UNIQUE,

            password TEXT,

            role TEXT
        )

    """)

    # Ajouter admin
    cursor.execute("""

        INSERT OR IGNORE INTO users
        (username, password, role)

        VALUES (?, ?, ?)

    """, (

        "admin",
        "admin123",
        "admin"
    ))

    conn.commit()

    conn.close()

    print("✅ Base créée.")


if __name__ == "__main__":

    initialiser_bd()