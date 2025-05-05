# TP 01 : Commandes de base sous Linux

## Introduction

Ce TP vous permettra de maîtriser les commandes Linux de base telles que `ls`, `cd`, `pwd`, `cp`, `mv`, `rm`, `mkdir`, `rmdir`, `chmod`, `chown`, `cat`, `less`, `head`, `tail`, `find`, `locate`. Ces commandes sont essentielles pour naviguer et manipuler les fichiers et répertoires sous Linux.

Toutes ces commandes sont expliquées dans mon guide sur [les commandes de
base](https://blog.stephane-robert.info/docs/admin-serveurs/linux/commandes/).

---

## 🔄 Rappels de commandes

- `ls` : liste les fichiers et répertoires du répertoire courant.
- `cd` : change de répertoire.
- `pwd` : affiche le chemin absolu du répertoire courant.
- `cp` : copie des fichiers ou répertoires.
- `mv` : déplace ou renomme des fichiers ou répertoires.
- `rm` : supprime des fichiers ou répertoires.
- `mkdir` : crée un nouveau répertoire.
- `rmdir` : supprime un répertoire vide.
- `chmod` : modifie les permissions d'un fichier ou répertoire.
- `chown` : change le propriétaire d'un fichier ou répertoire.
- `cat` : affiche le contenu d'un fichier.
- `less` : affiche le contenu d'un fichier page par page.
- `head` : affiche les premières lignes d'un fichier.
- `tail` : affiche les dernières lignes d'un fichier.
- `find` : recherche des fichiers dans une hiérarchie de répertoires.
- `locate` : recherche rapide de fichiers en utilisant une base de données.

## 📚 Utiliser l'aide intégrée

Avant de commencer, installez **tldr**, un outil qui fournit des exemples clairs pour les commandes.

Installez-le sur Debian/Ubuntu :

```bash
sudo apt update
sudo apt install tldr
```

Mettez à jour les pages locales :

```bash
tldr --update
```

Utilisation :

```bash
tldr cp
tldr mv
```

Vous pouvez aussi utiliser :

- **Manuel complet** :

```bash
man <commande>
```

- **Aide rapide** :

```bash
<commande> --help
```

Exemple :

```bash
man grep
grep --help
```

## 🔢 Tutoriels

### Exercice 1 : Navigation basique

Fichier utilisé : `fichiers/fichier_exercice1.txt`

1. Affichez le chemin absolu du répertoire courant :

```bash
pwd
```

Cette commande vous indique où vous vous situez dans l’arborescence des fichiers.

2. Listez le contenu de ce répertoire :

```bash
ls
```

Cela vous montre les fichiers et dossiers présents.

---

### Exercice 2 : Création et suppression

Fichier utilisé : `fichiers/fichier_exercice2.txt`

1. Déplacez-vous dans le répertoire `/tmp` :

```bash
cd /tmp
```

2. Créez un dossier `test` :

```bash
mkdir test
```

3. Supprimez ce dossier :

```bash
rmdir test
```

4. Revenez dans le répertoire précédent :

```bash
cd -
```

---

### Exercice 3 : Manipulation de fichiers

Fichier utilisé : `fichiers/fichier_exercice3.txt`

1. Copiez `fichier_exercice3.txt` vers un nouveau fichier `copie.txt` :

```bash
cp fichiers/fichier_exercice3.txt copie.txt
```

2. Renommez-le en `renomme.txt` :

```bash
mv copie.txt renomme.txt
```

3. Supprimez `renomme.txt` :

```bash
rm renomme.txt
```

---

### Exercice 4 : Affichage et recherche dans les fichiers

Fichier utilisé : `fichiers/fichier_exercice4.txt`

1. Affichez les 5 premières lignes du fichier :

```bash
head -n 5 fichiers/fichier_exercice4.txt
```

2. Affichez les 3 dernières lignes du fichier :

```bash
tail -n 3 fichiers/fichier_exercice4.txt
```

3. Affichez l’intégralité du fichier avec pagination :

```bash
less fichiers/fichier_exercice4.txt
```

---

### Exercice 5 : Permissions et propriétaires

Fichier utilisé : `fichiers/fichier_exercice5.txt`

1. Donnez les droits d’exécution au fichier :

```bash
chmod +x fichiers/fichier_exercice5.txt
```

2. Changez le propriétaire du fichier (nécessite sudo) :

```bash
sudo chown $USER fichiers/fichier_exercice5.txt
```

---

### Exercice 6 : Recherche de fichiers

1. Recherchez tous les fichiers `.txt` dans le répertoire courant et ses sous-répertoires :

```bash
find . -name "*.txt"
```

2. Recherchez les fichiers modifiés au cours des 7 derniers jours dans `/var/log` :

```bash
find /var/log -mtime -7
```

3. Utilisez `locate` pour trouver un fichier nommé `passwd` :

```bash
locate passwd
```

## 🎯 Challenge

Consultez le dossier [`challenge/`](./challenge/) pour réaliser un exercice final permettant de valider vos compétences à l'aide de tests automatisés.

