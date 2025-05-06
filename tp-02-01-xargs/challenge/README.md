# 🎯 Challenge Final : Maîtriser `xargs`

**Objectif :** Supprimer tous les fichiers `.txt` présents dans le dossier `../fichiers/` en utilisant `xargs` de manière sécurisée (en tenant compte des espaces dans les noms de fichiers).

## Consignes :

- Utilisez `find` avec `-print0` et `xargs -0` pour traiter les noms avec des espaces.
- Lancez la commande depuis la racine du projet (à côté du dossier `challenge/`).

## ✅ Critères de validation

Le challenge est validé automatiquement si les tests passent avec succès :

```bash
pytest -v
```

Exemple de sortie :

```plaintext
=== test session starts ===
platform linux -- Python 3.10.12, pytest-8.3.5, pluggy-1.5.0 -- /home/outscale/.local/share/pipx/venvs/pytest/bin/python
cachedir: .pytest_cache
rootdir: /home/outscale/Projets/linux-training/tp-02-01-xargs/challenge
plugins: testinfra-10.2.2
collected 1 item

tests/test_xargs.py::test_txt_files_deleted[local] PASSED                                               [100%]

==== 1 passed in 0.01s ====```
