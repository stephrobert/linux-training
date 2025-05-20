# 🧩 Challenge : Installation d'une version fixée d'un package

## 🎯 Objectif

Configurer un système Debian pour qu'il utilise un dépôt spécifique et installe
une version précise d'un paquet, en respectant des préférences définies.

## 📋 Instructions

1. Modifier le fichier `/etc/apt/sources.list` pour ajouter le dépôt suivant :

   ```bash
   deb http://deb.debian.org/debian buster main
   ```

2. Créer ou modifier le fichier `/etc/apt/preferences.d/nano` pour que le paquet `nano`
   soit installé en version `7.2-2` avec une priorité de `1001`.

3. Mettez à jour la liste des paquets et installez nano.

### ✅ Validation

Exécutez les tests avec la commande suivante :

```bash
cd tp-07-paquets-apt
pytest -v challenge/tests/test_tp.py
```

Vous devez obtenir un résultat similaire à celui-ci :

```bash
 pytest -v challenge/tests/test_tp.py
=== test session starts ===
platform linux -- Python 3.12.3, pytest-8.3.5, pluggy-1.6.0 -- /home/ubuntu/.local/share/pipx/venvs/pytest/bin/python
cachedir: .pytest_cache
rootdir: /home/ubuntu/linux-training/tp-07-paquets-apt
plugins: testinfra-10.2.2
collected 2 items

challenge/tests/test_tp.py::test_preferences[local] PASSED                                                      [ 50%]
challenge/tests/test_tp.py::test_nano_version[local] PASSED                                                     [100%]

=== 2 passed in 0.03s ===