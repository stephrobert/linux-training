import testinfra

def test_resultat1_existe_et_non_vide(host):
    f = host.file("resultat1.txt")
    assert f.exists, "resultat1.txt n'existe pas"
    assert f.size > 0, "resultat1.txt est vide"

def test_resultat2_existe_et_non_vide(host):
    f = host.file("resultat2.txt")
    assert f.exists, "resultat2.txt n'existe pas"
    assert f.size > 0, "resultat2.txt est vide"

def test_resultat3_existe_et_non_vide(host):
    f = host.file("resultat3.txt")
    assert f.exists, "resultat3.txt n'existe pas"
    assert f.size > 0, "resultat3.txt est vide"

def test_resultat4_existe_et_non_vide(host):
    f = host.file("resultat4.txt")
    assert f.exists, "resultat4.txt n'existe pas"
    assert f.size > 0, "resultat4.txt est vide"

def test_resultat5_existe_et_non_vide(host):
    f = host.file("resultat5.txt")
    assert f.exists, "resultat5.txt n'existe pas"
    assert f.size > 0, "resultat5.txt est vide"

def test_resultat5_contenu(host):
    f = host.file("resultat5.txt")
    assert f.contains("ALICE,31")
    assert f.contains("CHARLIE,35")
    assert f.content_string.count("ALICE,31") == 2
    assert f.content_string.count("CHARLIE,35") == 1
    assert len(f.content_string.strip().splitlines()) == 3
