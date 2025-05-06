# 🎯 Challenge : Création d'une arborescence avec les commandes Linux de base

## Objectif

Utilisez les commandes Linux de base pour créer l'arborescence suivante :

```bash
projet/
├── docs/
│   └── manuel.txt
├── src/
│   ├── main.sh
│   └── utils.sh
└── bin/
    └── script.sh
```

Vous devez créer cette arborescence dans le répertoire `challenge` de ce tP.

## Instructions

1. Créez le répertoire `projet` avec les sous-répertoires `docs`, `src` et `bin`.
2. Dans `docs`, créez un fichier `manuel.txt` contenant le texte : `Documentation du projet`.
3. Dans `src`, créez deux fichiers :
   - `main.sh` contenant le texte :

    ```bash
    #!/bin/bash
    echo "Programme principal"
    ```

   - `utils.sh` contenant le texte :

    ```bash
    #!/bin/bash
    echo "Fonctions utilitaires"
    ```

4. Copiez `main.sh` dans `bin` sous le nom `script.sh`.
5. Déplacez `utils.sh` dans `docs`.
6. Modifiez les permissions :
   - `main.sh` et `script.sh` doivent être lisibles et exécutables uniquement par le propriétaire.
   - `manuel.txt` doit être lisible par tous.
7. Changez le propriétaire de tous les fichiers et répertoires en `9001:9001`.
8. Utilisez `find` pour lister tous les fichiers `.sh` dans le répertoire `projet`.

## Validation

Retourner dans le dossier `challenge` et exécuter le script de validation :

```bash
pytest -v test.py
```

Si le script de validation passe sans erreur, vous avez réussi le challenge.
Vérifiez les étapes et corrigez les erreurs.

Tous les tests doivent passer pour valider le challenge.

```plaintext
=== test session starts ===
platform linux -- Python 3.9.22, pytest-8.3.5, pluggy-1.5.0 -- /home/bob/.pyenv/versions/3.9.22/bin/python3.9
cachedir: .pytest_cache
rootdir: /home/bob/Projets/linux-training/tp-01-navigation-fichiers/challenge
plugins: testinfra-10.2.2
collected 5 items

tests/test_tp.py::test_arborescence[local] PASSED        [ 20%]
tests/test_tp.py::test_fichiers_contenu[local] PASSED    [ 40%]
tests/test_tp.py::test_permissions[local] PASSED         [ 60%]
tests/test_tp.py::test_proprietaire[local] PASSED        [ 80%]
tests/test_tp.py::test_find[local] PASSED                [100%]

=== 5 passed in 0.34s ====