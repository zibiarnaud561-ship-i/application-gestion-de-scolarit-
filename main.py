from src.etudiant import Etudiant

# Exemple d’utilisation
e1 = Etudiant("Mbarga", "Jean-Paul", "21TIC042", "TIC")
e1.ajouter()

print("Liste des étudiants :", Etudiant.afficher_tous())

Etudiant.modifier("21TIC042", "Mbarga", "Jean-Paul", "Informatique")

Etudiant.supprimer("21TIC042")
from src.cours import Cours

# Création d’un cours
c1 = Cours("TIC101", "Développement Logiciel", 6)
c1.ajouter()

# Affichage
print("Liste des cours :", Cours.afficher_tous())

# Modification
Cours.modifier("TIC101", "Programmation Avancée", 8)

# Suppression
Cours.supprimer("TIC101")
from src.inscription import Inscription

# Exemple : inscrire l’étudiant avec id=1 au cours avec id=1
i1 = Inscription(etudiant_id=1, cours_id=1, note=15.5)
i1.ajouter()

# Affichage
print("Liste des inscriptions :", Inscription.afficher_toutes())

# Modification de la note
Inscription.modifier(inscription_id=1, nouvelle_note=17.0)

# Suppression
Inscription.supprimer(inscription_id=1)
from src.bulletin import Bulletin

# Générer le bulletin pour l’étudiant avec id=1
b1 = Bulletin(etudiant_id=1)
b1.generer_bulletin()
from src.auth import Auth

# Création d’un utilisateur admin
admin = Auth("admin1", "1234", "admin")
admin.register()

# Création d’un utilisateur étudiant
etu = Auth("etu1", "abcd", "etudiant")
etu.register()

# Test de connexion
print(Auth.login("admin1", "1234"))     # Connexion réussie (admin)
print(Auth.login("etu1", "abcd"))       # Connexion réussie (etudiant)
print(Auth.login("etu1", "wrong"))      # Échec de connexion
from src.auth import Auth
from src.etudiant import Etudiant
from src.cours import Cours
from src.inscription import Inscription
from src.bulletin import Bulletin

def menu_principal():
    print("\n=== Application de Gestion de Scolarité ===")
    print("1. Connexion")
    print("2. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        username = input("Nom d'utilisateur : ")
        password = input("Mot de passe : ")
        role = Auth.login(username, password)

        if "admin" in role:
            menu_admin()
        elif "etudiant" in role:
            menu_etudiant(username)
        else:
            print("Identifiants invalides.")
            menu_principal()
    elif choix == "2":
        print("Au revoir !")
    else:
        print("Choix invalide.")
        menu_principal()


def menu_admin():
    while True:
        print("\n=== Menu Admin ===")
        print("1. Gérer étudiants")
        print("2. Gérer cours")
        print("3. Gérer inscriptions")
        print("4. Retour")

        choix = input("Votre choix : ")

        if choix == "1":
            print("Liste des étudiants :", Etudiant.afficher_tous())
        elif choix == "2":
            print("Liste des cours :", Cours.afficher_tous())
        elif choix == "3":
            print("Liste des inscriptions :", Inscription.afficher_toutes())
        elif choix == "4":
            break
        else:
            print("Choix invalide.")


def menu_etudiant(username):
    print("\n=== Menu Étudiant ===")
    print("Bienvenue,", username)

    # Ici on suppose que l’étudiant est déjà inscrit avec un id connu
    etudiant_id = int(input("Entrez votre ID étudiant : "))
    bulletin = Bulletin(etudiant_id)
    bulletin.generer_bulletin()


if __name__ == "__main__":
    menu_principal()
