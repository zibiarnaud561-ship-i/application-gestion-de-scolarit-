from src.etudiant import Etudiant
from src.cours import Cours


# Ajouter étudiant
e1 = Etudiant(
    "Mbarga",
    "Jean-Paul",
    "21TIC042",
    "TIC"
)

e1.ajouter()


# Afficher étudiants
print("Liste des étudiants :")

print(Etudiant.afficher_tous())


# Ajouter cours
c1 = Cours(
    "INF101",
    "Programmation Python",
    5
)

c1.ajouter()