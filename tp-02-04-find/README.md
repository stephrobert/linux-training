# TP 02-03 : Manipuler les fichiers avec `find`

## Introduction

La commande `find` permet de rechercher efficacement des fichiers et des répertoires sous Linux, en utilisant des critères comme le nom, la taille, la date de modification, les permissions, etc. C’est un outil incontournable pour administrer un système et automatiser des tâches.

---

## 📚 Résumé de la documentation technique

- **Nom** : `find`
- **Type** : Commande de recherche
- **Fonctionnalités principales** :
  - Recherche par nom (`-name`, `-iname`)
  - Filtrage par type (`-type f`, `-type d`, etc.)
  - Recherche par taille (`-size`)
  - Recherche par date (`-mtime`, `-ctime`, `-atime`)
  - Recherche par permissions (`-perm`)
  - Recherche par propriétaire (`-user`, `-group`)
  - Exécution d’actions (`-exec`)
- **Syntaxe de base** :

  ```bash
  find [chemin] [conditions] [actions]
  ```

  - `[chemin]` : Répertoire de départ
  - `[conditions]` : Critères de sélection
  - `[actions]` : Ce qu'on fait sur les résultats

- **Variables et options utiles** :
  - `.` : répertoire courant
  - `{}` : représente le fichier courant
  - `\;` : fin de la commande après `-exec`

Plus d'informations sur le [guide dédié à la commande `find`](https://blog.stephane-robert.info/docs/admin-serveurs/linux/find/).

## 🧪 Exercices

### Exercice 1 : Recherche par nom

**Objectif** : Rechercher des fichiers par nom, avec et sans casse.

**Fichier fourni** : `fichiers/rapport1.txt`, `fichiers/rapport2.TXT`

**Commande à utiliser** :

```bash
find . -name "rapport1.txt"
find . -iname "rapport2.txt"
```

**Explication** :

- `-name` : recherche sensible à la casse.
- `-iname` : recherche insensible à la casse.

---

### Exercice 2 : Filtrage par type de fichier

**Objectif** : Rechercher des fichiers réguliers ou des liens symboliques.

**Fichier fourni** : `fichiers/script.sh`, `fichiers/lien_sym`

**Commande à utiliser** :

```bash
find . -type f
find . -type d
```

**Explication** :

- `-type f` : fichiers classiques
- `-type d` : répertoires

---

### Exercice 3 : Recherche par taille

**Objectif** : Trouver des fichiers trop gros ou vides.

**Fichier fourni** : `fichiers/archive.log`, `fichiers/vide.txt`

**Commande à utiliser** :

```bash
find . -type f -size +100k
find . -type f -empty
```

**Explication** :

- `-size +100k` : plus de 100 Ko
- `-empty` : fichiers vides

---

### Exercice 4 : Recherche par date

**Objectif** : Identifier des fichiers récents ou anciens.

**Fichier fourni** : `fichiers/ancien.log`

**Commande à utiliser** :

```bash
find . -type f -mtime +7
find . -type f -mtime -1
```

**Explication** :

- `-mtime +7` : modifiés il y a plus de 7 jours
- `-mtime -1` : modifiés dans les dernières 24 heures

---

### Exercice 5 : Exécuter des actions sur les fichiers trouvés

**Objectif** : Modifier les permissions des fichiers `.txt`.

**Fichier fourni** : `fichiers/secret.txt`

**Commande à utiliser** :

```bash
find . -type f -name "*.txt" -exec chmod 600 {} \;
```

**Explication** :

- `-exec` : exécute une commande sur chaque fichier
- `chmod 600` : permissions lecture/écriture pour l’utilisateur

---

## 🏁 Challenge à valider

Pour accéder au challenge final, consultez le fichier `challenge/README.md`.

---

Ce TP vous permettra de comprendre et d’utiliser efficacement la commande `find` pour automatiser vos recherches et traitements de fichiers sur un système Linux.
