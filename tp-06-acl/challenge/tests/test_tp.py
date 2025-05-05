import testinfra

def test_document1_acl(host):
    # Vérifie que le groupe 'stagiaires' a le droit en lecture seule sur document1.txt
    cmd = host.run("getfacl document1.txt")
    assert "group:stagiaires:r--" in cmd.stdout, "Le groupe 'stagiaires' n'a pas les bons droits sur document1.txt"

def test_document2_acl(host):
    # Vérifie que l'utilisateur 'etudiant' a le droit en écriture uniquement sur document2.txt
    cmd = host.run("getfacl document2.txt")
    assert "user:etudiant:-w-" in cmd.stdout, "L'utilisateur 'etudiant' n'a pas les bons droits sur document2.txt"

def test_partage_default_acl(host):
    # Vérifie qu'il y a une ACL par défaut pour le groupe 'stagiaires' sur le dossier partage/
    cmd = host.run("getfacl -d partage")
    assert "group:stagiaires:rw-" in cmd.stdout, "L'ACL par défaut sur le dossier partage/ n'est pas correcte"

def test_partage_contents(host):
    # Vérifie la présence du fichier document3.txt
    f = host.file("partage/document3.txt")
    assert f.exists, "Le fichier partage/document3.txt est manquant"
    # Vérifie la présence du dossier dossier1/
    d = host.file("partage/dossier1")
    assert d.is_directory, "Le dossier partage/dossier1/ est manquant"
