import sqlite3

class Auth:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    # --- CREATE USER ---
    def register(self):
        conn = sqlite3.connect("scolarite.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (username, password, role)
            VALUES (?, ?, ?)
        """, (self.username, self.password, self.role))
        conn.commit()
        conn.close()

    # --- LOGIN ---
    @staticmethod
    def login(username, password):
        conn = sqlite3.connect("scolarite.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT role FROM users WHERE username=? AND password=?
        """, (username, password))
        result = cursor.fetchone()
        conn.close()

        if result:
            return f"Connexion réussie ({result[0]})"
        else:
            return "Échec de connexion : identifiants invalides"
