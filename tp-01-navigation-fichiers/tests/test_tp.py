import os

# Définir le chemin du dossier à tester
DOSSIER_TP = os.path.join(os.path.dirname(__file__), "..", "mon-premier-dossier")

def test_dossier_existe():
    assert os.path.isdir(DOSSIER_TP)

def test_fichiers_presents():
    fichiers = ["fichier1.txt", "fichier3_renomme.txt", "fruits.txt"]
    for fichier in fichiers:
        chemin = os.path.join(DOSSIER_TP, fichier)
        assert os.path.isfile(chemin)

def test_contenu_fichier1():
    chemin = os.path.join(DOSSIER_TP, "fichier1.txt")
    with open(chemin) as f:
        contenu = f.read()
    assert "test de contenu" in contenu

def test_contenu_fruits():
    chemin = os.path.join(DOSSIER_TP, "fruits.txt")
    with open(chemin) as f:
        contenu = f.read()
    assert "banana" in contenu and "apple" in contenu
