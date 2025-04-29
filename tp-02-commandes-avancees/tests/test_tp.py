import os

DOSSIER = os.path.join(os.path.dirname(__file__), "..", "mon-second-dossier", "data")

def test_crochets_format():
    chemin = os.path.join(DOSSIER, "crochets.txt")
    assert os.path.isfile(chemin)
    with open(chemin) as f:
        lignes = f.readlines()
    assert lignes[0].strip().startswith("[") and lignes[0].strip().endswith("]")

def test_debut_fruits():
    chemin = os.path.join(DOSSIER, "debut_fruits.txt")
    assert os.path.isfile(chemin)
    with open(chemin) as f:
        contenu = f.read().splitlines()
    assert all(len(l) == 3 for l in contenu)

def test_fruits_tries():
    chemin = os.path.join(DOSSIER, "fruits_tries.txt")
    assert os.path.isfile(chemin)
    with open(chemin) as f:
        lignes = f.read().splitlines()
    assert lignes == sorted(lignes)

def test_fruits_uniques():
    chemin = os.path.join(DOSSIER, "fruits_uniques.txt")
    assert os.path.isfile(chemin)
    with open(chemin) as f:
        lignes = f.read().splitlines()
    assert len(lignes) == len(set(lignes))

def test_compte_fruits():
    chemin = os.path.join(DOSSIER, "compte_fruits.txt")
    assert os.path.isfile(chemin)
    with open(chemin) as f:
        lignes = f.readlines()
    assert all(l.strip()[0].isdigit() for l in lignes)

def test_journal_execution():
    chemin = os.path.join(DOSSIER, "journal_execution.txt")
    assert os.path.isfile(chemin)
    with open(chemin) as f:
        contenu = f.read()
    assert any(char.isdigit() for char in contenu)
