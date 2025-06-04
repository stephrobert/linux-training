import os
import subprocess

def test_commande_existence():
    assert os.path.exists("challenge/commande.txt"), "Le fichier commande.txt est manquant"

def test_log_suppression_and_gz_creation():
    original = "fichiers/gros.log"
    compressed = "fichiers/gros.log.gz"

    # Préconditions
    assert os.path.exists("challenge/commande.txt"), "commande.txt est requis"

    # Vérifications post-exécution
    assert not os.path.exists(original), "Le fichier gros.log aurait dû être supprimé"
    assert os.path.exists(compressed), "Le fichier gros.log.gz aurait dû être créé"
