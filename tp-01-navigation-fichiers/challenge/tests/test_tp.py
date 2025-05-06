import os
import pytest
import testinfra

def test_arborescence(host):
    projet = host.file("projet")
    assert projet.is_directory

    docs = host.file("projet/docs")
    src = host.file("projet/src")
    bin_dir = host.file("projet/bin")
    assert docs.is_directory
    assert src.is_directory
    assert bin_dir.is_directory

def test_fichiers_contenu(host):
    manuel = host.file("projet/docs/manuel.txt")
    assert manuel.exists
    assert manuel.contains("Documentation du projet")

    main = host.file("projet/src/main.sh")
    assert main.exists
    assert main.contains('echo "Programme principal"')

    utils = host.file("projet/docs/utils.sh")
    assert utils.exists
    assert utils.contains('echo "Fonctions utilitaires"')

    script = host.file("projet/bin/script.sh")
    assert script.exists
    assert script.contains('echo "Programme principal"')

def test_permissions(host):
    main = host.file("projet/src/main.sh")
    script = host.file("projet/bin/script.sh")
    manuel = host.file("projet/docs/manuel.txt")

    assert main.mode == 0o700
    assert script.mode == 0o700
    assert manuel.mode & 0o444 == 0o444  # Lisible par tous

def test_proprietaire(host):
    for path in [
        "projet",
        "projet/docs",
        "projet/src",
        "projet/bin",
        "projet/docs/manuel.txt",
        "projet/docs/utils.sh",
        "projet/src/main.sh",
        "projet/bin/script.sh",
    ]:
        fichier = host.file(path)
        assert fichier.group == "adm"

def test_find(host):
    cmd = host.run("find projet -name '*.sh'")
    assert "main.sh" in cmd.stdout
    assert "utils.sh" in cmd.stdout
    assert "script.sh" in cmd.stdout


