# 🎯 Challenge Final – TP ACL Linux

## Objectif

Configurer correctement les ACL sur les fichiers fournis afin de répondre aux critères suivants.

## À faire

1. Sur le fichier `document1.txt` :
   - Donnez au groupe `stagiaires` un accès en lecture seule.

2. Sur le fichier `document2.txt` :
   - Donnez à l’utilisateur `etudiant` le droit **en écriture uniquement** (sans lecture ni exécution).

3. Sur le dossier `partage/` :
   - Ajoutez une ACL par défaut pour que tous les fichiers créés ici soient lisibles et modifiables par le groupe `stagiaires`.

4. Dans le dossier `partage/` :
   - Créez un fichier `document3.txt` et un dossier `dossier1/`.

## Instructions

- Utilisez les commandes `setfacl` et `getfacl` pour configurer les ACL.
- Vérifiez que les droits sont correctement appliqués avec `getfacl`.

## Validation

Ce challenge est validé automatiquement grâce aux tests présents dans le dossier `tests/`.

Pour lancer la validation :

```bash
pytest -v
````

