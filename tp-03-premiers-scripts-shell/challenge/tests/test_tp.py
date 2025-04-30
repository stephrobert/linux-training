import os
import pytest

def test_script_existe(host):
    script = host.file("analyse_utilisateurs.sh")
    assert script.exists, "Le script analyse_utilisateurs.sh n'existe pas."

def test_script_executable(host):
    script = host.file("analyse_utilisateurs.sh")
    assert script.mode & 0o111, "Le script analyse_utilisateurs.sh n'est pas exécutable."

def test_sortie_terminal(host):
    cmd = host.run("./analyse_utilisateurs.sh")
    assert cmd.rc == 0, "Le script s'est terminé avec une erreur."
    assert "Nombre total d'utilisateurs" in cmd.stdout, "Le nombre d'utilisateurs n'est pas affiché."
    assert "Âge moyen" in cmd.stdout, "L'âge moyen n'est pas affiché."
    assert "Utilisateur le plus âgé" in cmd.stdout, "L'utilisateur le plus âgé n'est pas affiché."

def test_majeurs_txt(host):
    majeurs = host.file("majeurs.txt")
    assert majeurs.exists, "Le fichier majeurs.txt n'existe pas."
    contenu = majeurs.content_string.strip().splitlines()
    assert len(contenu) >= 1, "Le fichier majeurs.txt est vide ou mal rempli."
    assert all(nom for nom in contenu), "Certaines lignes de majeurs.txt sont vides."

def test_utilisateur_plus_age(host):
    cmd = host.run("./analyse_utilisateurs.sh")
    assert "Stéphane" in cmd.stdout or "Stephane" in cmd.stdout, "L'utilisateur le plus âgé attendu n'est pas affiché."
