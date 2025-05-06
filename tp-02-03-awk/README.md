# TP 02-03 : Manipuler des fichiers texte avec `awk`

## Introduction

La commande `awk` est un outil puissant pour le traitement de texte en ligne de
commande. Elle permet de lire des fichiers ligne par ligne, de découper chaque
ligne en champs (colonnes) et d'appliquer des actions conditionnelles sur ces
champs. C'est un langage de programmation à part entière, conçu pour
l'extraction et la transformation de données textuelles. Lisez la documentation
: [Manipuler des fichiers texte avec
awk](https://blog.stephane-robert.info/docs/admin-serveurs/linux/awk/).

---

## 📚 Résumé de la documentation technique

- **Nom** : `awk`
- **Type** : Langage de traitement de texte
- **Fonctionnalités principales** :
  - Extraction de champs spécifiques
  - Filtrage de lignes selon des motifs
  - Réalisation de calculs (sommes, moyennes, comptages)
  - Reformatage ou restructuration de fichiers texte
- **Syntaxe de base** :

  ```bash
  awk 'motif { action }' fichier
  ```

  - **motif** : Condition pour exécuter l'action (optionnelle)
  - **action** : Opération à réaliser sur la ligne
- **Variables intégrées** :
  - `$0` : Ligne entière
  - `$1`, `$2`, ... : Champs de la ligne
  - `NF` : Nombre de champs dans la ligne
  - `NR` : Numéro de la ligne en cours
  - `FS` : Séparateur de champs (par défaut, espace ou tabulation)

---

## 🧪 Exercices

### Exercice 1 : Extraire des champs spécifiques

**Objectif** : Extraire les noms d'utilisateurs et leurs identifiants depuis un
fichier CSV.

**Fichier fourni** : `fichiers/utilisateurs.csv`

**Commande à utiliser** :

```bash
awk -F';' '{ print $1, $3 }' fichiers/utilisateurs.csv
```

**Explication** :

- `-F';'` : Spécifie que le séparateur de champs est le point-virgule.
- `$1` : Premier champ (nom d'utilisateur).
- `$3` : Troisième champ (identifiant).

---

### Exercice 2 : Filtrer des lignes selon un motif

**Objectif** : Afficher les lignes contenant le mot "ERROR" dans un fichier de
logs.

**Fichier fourni** : `fichiers/logs.txt`

**Commande à utiliser** :

```bash
awk '/ERROR/' fichiers/logs.txt
```

**Explication** :

- `/ERROR/` : Motif recherché dans chaque ligne.
- Si le motif est trouvé, la ligne est affichée.

---

### Exercice 3 : Compter le nombre de champs par ligne

**Objectif** : Afficher le nombre de champs pour chaque ligne d'un fichier.

**Fichier fourni** : `fichiers/passwd.txt`

**Commande à utiliser** :

```bash
awk -F':' '{ print "Ligne " NR ": " NF " champs" }' fichiers/passwd.txt
```

**Explication** :

- `-F':'` : Spécifie que le séparateur de champs est le deux-points.
- `NR` : Numéro de la ligne en cours.
- `NF` : Nombre de champs dans la ligne.

---

### Exercice 4 : Calculer la somme d'une colonne

**Objectif** : Calculer le total des ventes à partir d'un fichier CSV.

**Fichier fourni** : `fichiers/ventes.csv`

**Commande à utiliser** :

```bash
awk -F',' '{ total += $2 } END { print "Total des ventes:", total }' fichiers/ventes.csv
```

**Explication** :

- `-F','` : Spécifie que le séparateur de champs est la virgule.
- `total += $2` : Ajoute la valeur du deuxième champ à la variable `total`.
- `END { print ... }` : Après avoir lu toutes les lignes, affiche le total.

---

### Exercice 5 : Reformater des lignes

**Objectif** : Afficher le propriétaire et le nom de chaque fichier dans un
format spécifique.

**Fichier fourni** : `fichiers/fichiers.txt`

**Commande à utiliser** :

```bash
awk '{ print "Propriétaire: " $3 ", Fichier: " $9 }' fichiers/fichiers.txt
```

**Explication** :

- `$3` : Troisième champ (propriétaire du fichier).
- `$9` : Neuvième champ (nom du fichier).
- Affiche une chaîne formatée avec les informations souhaitées.

---

## 🏁 Challenge à valider

Pour accéder au challenge final, consultez le fichier `challenge/README.md`.

---

Ce TP vous permettra de maîtriser les bases de la commande `awk` et de
l'appliquer à des cas concrets de traitement de fichiers texte.