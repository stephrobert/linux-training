# 🏁 Challenge final : Nettoyage automatisé avec `find`

## 🎯 Objectif

Vous devez écrire une **commande `find`** qui identifie et supprime certains fichiers dans le répertoire `fichiers/`.

## 🛠️ Consignes

Vous devez créer un fichier nommé `commande.txt` dans le répertoire
`challenge/`. Ce fichier doit contenir une commande `find` qui répond aux
critères suivants :

1. **Recherche tous les fichiers `.log` de plus de 1 Mo** dans `fichiers/` ;
2. **Les compresse automatiquement** ;
3. **Affiche les chemins des fichiers supprimés** (grâce à `-print`).

Exemple attendu dans `commande.txt` :

```bash
find fichiers/ -type f
```

Exécutez la commande pour vérifier qu'elle fonctionne correctement.

## ✅ Critères de validation

Le challenge est validé automatiquement si les tests passent avec succès :

```bash
pytest -v
```

Exemple de sortie :

```plaintext
=== test session starts ===
platform linux -- Python 3.9.22, pytest-8.3.5
plugins: testinfra-10.2.2
collected 2 items

tests/test_arborescence.py::test_commande_existence PASSED    [ 50%]
tests/test_arborescence.py::test_commande_find_effect PASSED  [100%]

==== 2 passed in 0.02s ====
```
