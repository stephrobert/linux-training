# TP 02 : Commandes avancées Linux

## 🧠 Introduction

Ce TP vous permettra de maîtriser des commandes Linux avancées essentielles pour
l'administration système. Vous apprendrez à manipuler des fichiers, gérer des
processus et analyser l'utilisation du disque.

Ces commandes sont expliquées dans mon guide sur [les commandes
avancées](https://blog.stephane-robert.info/docs/admin-serveurs/linux/commandes-avancees/).

## 📚 Résumé des commandes abordées

- **`uname`** : affiche des informations sur le système.
- **`free`** : affiche l'utilisation de la mémoire.
- **`diff`** : compare le contenu de deux fichiers.
- **`ps`** : affiche les processus en cours.
- **`top`** : affiche les processus en temps réel.
- **`cut`** : extrait des sections de lignes de fichiers.
- **`tr`** : traduit ou supprime des caractères.
- **`paste`** : fusionne des lignes de fichiers.
- **`join`** : joint des lignes de deux fichiers sur une clé commune.
- **`comm`** : compare deux fichiers ligne par ligne.
- **`nl`** : numérote les lignes d'un fichier.
- **`tee`** : lit l'entrée standard et écrit dans un fichier et la sortie
  standard.
- **`rev`** : inverse les lignes caractère par caractère.
- **`fold`** : plie les lignes longues.
- **`sed`** : édite des fichiers en ligne de commande.
- **`awk`** : traite et analyse des fichiers texte.

## 🧪 Exercices

### Exercice 1 : Afficher des informations sur le système

**Objectif** : Utiliser `uname` pour afficher des informations sur le système.

**Commande** :

```bash
uname -a
```

**Explication** : `uname -a` affiche toutes les informations disponibles sur le
système.

**Tester les autres options de `uname`** : `-a`, `-s`, `-r`, `-v`, `-m`, `-p`,
`-i`, `-o`

---

### Exercice 2 : Afficher l'utilisation de la mémoire

**Objectif** : Utiliser `free` pour afficher l'utilisation de la mémoire.

**Commande** :

```bash
free -h
```


**Explication** : `free -h` affiche l'utilisation de la mémoire en format
lisible.

**Tester les autres options de `free`** `-h`, `-m`, `-g`

---

### Exercice 3 : Comparer deux fichiers

**Fichiers** : `fichiers/exercice3a.txt`, `fichiers/exercice3b.txt`

**Objectif** : Utiliser `diff` pour comparer deux fichiers.

**Commande** :

```bash
diff fichiers/exercice3a.txt fichiers/exercice3b.txt
2c2
< ligne2
---
> ligneModifiee
```

**Explication** :

- `2c2` : indique que **la ligne 2** du premier fichier est **changée** (`c`
  pour "change") par rapport à la ligne 2 du second fichier.
- `< ligne2` : montre le contenu de la ligne 2 dans le **premier fichier**
  (`exercice3a.txt`) — ici : `ligne2`.
- `>` ligneModifiee` : montre le contenu de la ligne 2 dans le **second
  fichier** (`exercice3b.txt`) — ici : `ligneModifiee`.

**Tester les autres options de `diff`** : `-u`, `-c`, `-y`

---

### Exercice 4 : Afficher les processus en cours

**Objectif** : Utiliser `ps` pour afficher les processus en cours.

**Commandes** :

```bash
ps aux
```

**Explication** : `ps aux` affiche tous les processus en cours.

**Tester les autres options de `ps`** : `a`, `u`, `x`;

La commande ps affiche les processus en cours d'exécution sur le système. Les
options `a`, `u` et `x` permettent d'afficher des informations détaillées sur
les processus, y compris ceux qui n'ont pas de terminal associé.

### Exercice 5 : Manipuler des fichiers texte

#### 🧪 Exercice 5.1 : Extraire et transformer des colonnes

**Fichier** : `fichiers/exercice5.txt` (format CSV : `nom,age`)

**Objectif** : Extraire les prénoms et les convertir en majuscules.

**Commandes** :

```bash
cut -d',' -f1 fichiers/exercice5.txt | tr 'a-z' 'A-Z'
```

**Explication** :

- `cut -d',' -f1` : extrait la première colonne, ici les prénoms.
- `tr 'a-z' 'A-Z'` : transforme les minuscules en majuscules.

---

#### 🧪 Exercice 5.2 : Rechercher et remplacer dans un fichier

**Fichier** : `fichiers/exercice5.txt`

**Objectif** : Remplacer tous les âges "30" par "31".

**Commande** :

```bash
sed 's/30/31/g' fichiers/exercice5.txt
```

**Explication** :

- `sed` permet de faire des remplacements avec des expressions régulières.
- Ici, on remplace toutes les occurrences de `30` par `31`.

---

#### 🧪 Exercice 5.3 : Filtrer et numéroter des lignes

**Fichier** : `fichiers/exercice5.txt`

**Objectif** : Afficher uniquement les personnes âgées de plus de 30 ans et
numéroter les lignes.

**Commande** :

```bash
awk -F',' '$2 > 30' fichiers/exercice5.txt | nl
```

**Explication** :

- `awk -F',' '$2 > 30'` : filtre les lignes où l'âge (2ᵉ champ) est supérieur à
  30.
- `nl` : numérote les lignes.

---

## 🏁 Challenge à valider

Consultez le dossier [`challenge/`](./challenge/) pour réaliser un exercice
final permettant de valider vos compétences à l'aide de tests automatisés.

## Aller plus loin

J'ai commencé à rédiger des TP sur certaines de ces commandes. Vous pouvez
trouver ces TP dans les sous-dossiers suivant :

- [xargs](https://github.com/stephrobert/linux-training/tree/main/tp-02-1-xargs)
- [awk](https://github.com/stephrobert/linux-training/tree/main/tp-02-3-awk)

D'autres TP seront ajoutés au fur et à mesure de mes avancées.