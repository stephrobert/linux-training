# 🛠️ TP 02-02 : Maîtriser la commande `sed`

## Introduction

Dans ce TP, vous apprendrez à utiliser la commande `sed` pour automatiser des
modifications de texte directement depuis la ligne de commande. Vous découvrirez
comment rechercher, remplacer, supprimer ou insérer des lignes sans ouvrir le
moindre fichier manuellement. La maîtrise de `sed` est un atout pour toute
personne qui gère des fichiers texte (logs, configurations, exports CSV…).

**Objectif :** savoir modifier rapidement et efficacement du contenu texte avec
`sed`.

## Résumé rapide

* **`sed 's/ancien/nouveau/' fichier`** : remplacer la première occurrence par
  ligne.
* **`sed 's/ancien/nouveau/g' fichier`** : remplacer toutes les occurrences.
* **`sed '/motif/d' fichier`** : supprimer les lignes contenant un motif.
* **`sed '3i\\Texte' fichier`** : insérer du texte avant la 3e ligne.
* **`sed '5c\\Nouvelle ligne' fichier`** : remplacer entièrement la 5e ligne.
* **Option `-i`** : modifier le fichier en place.
* **Scripts sed** : regrouper plusieurs commandes dans un fichier et les
  appliquer avec `-f`.

👉 [Documentation complète ici](https://blog.stephane-robert.info/docs/admin-serveurs/linux/sed/)

---

## Exercices

### 1 Remplacer un mot simple

**Fichier :** `fichiers/serveur.conf`

* Remplacez toutes les occurrences de `localhost` par `127.0.0.1`.

**Commande attendue :**

```bash
sed 's/localhost/127.0.0.1/g' fichiers/serveur.conf
```

---

### 2 Supprimer des lignes inutiles

**Fichier :** `fichiers/logs.txt`

* Supprimez toutes les lignes vides.
* Supprimez toutes les lignes contenant le mot `DEBUG`.

**Commandes attendues :**

```bash
sed '/^$/d' fichiers/logs.txt
sed '/DEBUG/d' fichiers/logs.txt
```

---

### 3 Ajouter un entête automatique

**Fichier :** `fichiers/report.csv`

* Ajoutez la ligne suivante avant la première ligne :

`# Rapport généré automatiquement`

**Commande attendue :**

```bash
sed '1i\\# Rapport généré automatiquement' fichiers/report.csv
```

---

### 4 Remplacer un bloc entier

**Fichier :** `fichiers/apache.conf`

* Remplacez toutes les lignes entre `<VirtualHost>` et `</VirtualHost>` par :

`# Bloc supprimé par sécurité`

**Commande attendue :**

```bash
outscale@dev:~/Projets/linux-training/tp-02-02-sed$ sed '/<VirtualHost.*>/,/<\/VirtualHost>/c\# Bloc supprimé par sécurité' fichiers/apache.conf
```

---

### 5 Utiliser un fichier de script sed

**Fichier :** `fichiers/users.txt` **Script sed :** `modifs.sed`

* Le fichier `modifs.sed` contient :

  ```
  s/admin/root/g
  /^#/d
  1i\\# Liste des utilisateurs
  ```
* Appliquez ces modifications sur `users.txt`.

**Commande attendue :**

```bash
sed -f modifs.sed fichiers/users.txt
```

---

## 🔥 Challenge à valider

Rendez-vous dans le dossier [`challenge/`](./challenge/README.md) pour relever
le défi final 🚀 !
