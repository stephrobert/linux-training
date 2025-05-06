# 🛠️ TP 02-01 : Maîtriser la commande `xargs`

## Introduction

La commande `xargs` est un outil incontournable lorsqu'il s'agit de traiter des
listes d'arguments complexes dans un terminal Linux. Elle permet de transformer
une entrée standard (stdin) en arguments pour une autre commande, automatisant
ainsi des tâches répétitives et évitant des erreurs classiques comme *"argument
list too long"*. Elle est fréquemment utilisée avec des commandes comme `find`,
`grep`, ou `rm`.

## Résumé de la documentation

* **Syntaxe de base** :

  ```bash
  commande_qui_genere | xargs commande_a_executer
  ```

* **Fonctionnement par défaut** : utilise `echo` si aucune commande n'est
  précisée.
* **Options clés** :

  * `-n` : limite le nombre d'arguments par commande.
  * `-p` : demande confirmation avant chaque exécution.
  * `-I` : remplace un jeton par l'argument dans la commande.
  * `-0` : gère les noms de fichiers avec caractères spéciaux (via `find
    -print0`).
  * `-t` : affiche la commande exécutée (debug).
* **Bonnes pratiques** :

  * Tester avec `echo` avant d'exécuter des commandes destructives.
  * Toujours gérer les espaces spéciaux avec `-0`.

👉 [Documentation source](https://blog.stephane-robert.info/docs/admin-serveurs/linux/xargs/)

## Exercices pratiques

### Exercice 1 - Exécuter une commande simple

**Objectif** : Lister les fichiers mentionnés dans
`fichiers/liste_fichiers.txt`.

**Commande attendue** :

```bash
cat fichiers/liste_fichiers.txt | xargs ls -l
```

💡 *Explication* : `cat` lit le fichier contenant des noms de fichiers, et
`xargs` les passe à `ls -l` pour afficher leurs détails.

---

### Exercice 2 - Limiter le nombre d'arguments par commande

**Objectif** : Tester la limitation à 2 fichiers par exécution.

**Commande attendue** :

```bash
echo "un deux trois quatre cinq" | xargs -n 2 echo
```

💡 *Explication* : L'option `-n 2` force `xargs` à exécuter `echo` avec 2
arguments à la fois.

---

### Exercice 3 - Déplacer des fichiers avec insertion

**Objectif** : Déplacer les fichiers listés dans `liste_fichiers.txt` vers
`/tmp/` en gardant leur nom.

**Commande attendue** :

```bash
mkdir /tmp/fichiers
cat fichiers/liste_fichiers.txt | xargs -I {} mv {} /tmp/{}
ls /tmp/fichiers
```

💡 *Explication* : `-I {}` remplace `{}` par chaque nom de fichier, pour
personnaliser la commande.

---

### Exercice 4 - Supprimer des fichiers avec confirmation

**Objectif** : Supprimer les fichiers listés dans
`fichiers/fichiers_avec_espaces.txt` avec confirmation.

**Commande attendue** :

```bash
cat fichiers/fichiers_avec_espaces.txt | xargs -p rm
```

💡 *Explication* : `-p` vous demande de confirmer avant chaque suppression.

---

### Exercice 5 - Gérer les noms de fichiers complexes

**Objectif** : Supprimer les fichiers `.txt` qui peuvent contenir des espaces
dans leur nom.

**Commande attendue** :

```bash
find fichiers/ -name "*.txt" -print0 | xargs -0 rm
```

💡 *Explication* : On utilise `-print0` (séparateur nul) et `-0` pour éviter les
erreurs avec des espaces ou caractères spéciaux.

---

## 🚩 Challenge à valider

👉 Consultez les consignes dans [`challenge/README.md`](./challenge/README.md)
pour le challenge final !

Bonne pratique 💪 !
