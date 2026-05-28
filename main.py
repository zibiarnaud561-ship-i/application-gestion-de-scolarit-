import sys

from PyQt6.QtWidgets import QApplication

from ui.accueil import FenetreAccueil


# Créer application
app = QApplication(sys.argv)

# Créer fenêtre accueil
fenetre = FenetreAccueil()

# Afficher fenêtre
fenetre.show()

# Exécuter application
sys.exit(app.exec())