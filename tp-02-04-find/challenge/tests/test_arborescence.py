import os
import subprocess

def test_commande_existence():
    assert os.path.exists("challenge/commande.txt"), "Le fichier commande.txt est manquant"

def test_commande_find_effect(tmp_path):
    # Préparer un environnement de test dans un dossier temporaire
    test_dir = tmp_path / "fichiers"
    test_dir.mkdir()

    # Fichier .log de plus de 1 Mo
    large_log = test_dir / "gros.log"
    large_log.write_bytes(b"x" * 1024 * 1025)  # ~1 Mo

    # Fichier .log petit (ne doit pas être supprimé)
    small_log = test_dir / "petit.log"
    small_log.write_text("log petit")

    # Fichier non .log
    autre = test_dir / "autre.txt"
    autre.write_text("autre")

    # Lire la commande
    with open("challenge/commande.txt") as f:
        commande = f.read().strip()

    # Remplacer le chemin 'fichiers/' par notre dossier temporaire
    commande = commande.replace("fichiers/", str(test_dir) + "/")

    # Exécuter la commande dans le shell
    subprocess.run(commande, shell=True, check=True)

    # Vérifier les effets
    assert not large_log.exists(), "Le fichier gros.log n'a pas été supprimé"
    assert small_log.exists(), "Le fichier petit.log ne devait pas être supprimé"
    assert autre.exists(), "Le fichier autre.txt ne devait pas être supprimé"
