Voici la nouvelle version **complète**, enrichie et corrigée selon tes instructions :
- **Installation de `tldr`** proposée,
- **Suppression** des commandes système inutiles (`hostname`, `uptime`, `date`, etc.),
- **Garde uniquement** `cal` pour l'information calendrier.

---

# TP : Les Commandes de Base Linux — **Naviguer, manipuler et explorer le système de fichiers**

## Objectif

Apprendre à :
- Se déplacer dans l'**arborescence Linux**,
- **Créer, copier, déplacer, renommer et supprimer** des fichiers et des dossiers,
- **Lire, rechercher, compter** et **analyser** du contenu texte,
- Utiliser l'**aide en ligne** efficacement.

**Remarque** : Ce TP est entièrement guidé. Dans les suivants, **vous devrez chercher les informations vous-même**. Donc n'hésitez pas à vous poser des questions pour essayer de comprendre ce qui se passe.

---

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

---

## 🧭 Se repérer dans le système

### 1. Vérifier où vous êtes

```bash
pwd
```

Afficher l'utilisateur connecté :

```bash
whoami
```

Afficher l'identifiant utilisateur :

```bash
id
```

Le resultat de `id` doit être `uid=1000(votre_nom_utilisateur)
gid=1000(votre_nom_utilisateur)`, puis d'autres groupes.

### 2. Explorer l'environnement

Lister les fichiers visibles et cachés :

```bash
ls
ls -a
ls -lh
```

Afficher les permissions et propriétaires :

```bash
ls -l
```

### 3. Se déplacer dans l'arborescence

Aller dans `/tmp`, puis revenir au répertoire personnel :

```bash
cd /tmp
pwd
cd ~
pwd
```

---

## 📁 Manipuler les fichiers et répertoires

### 1. Créer un dossier de travail

```bash
cd ~/linux-training/tp-01-navigation-fichiers
mkdir mon-premier-dossier
cd mon-premier-dossier
```

Créer un sous-dossier :

```bash
mkdir sous-dossier
```

Créer plusieurs fichiers rapidement :

```bash
touch fichier1.txt fichier2.txt fichier3.txt
```

Afficher l'état actuel :

```bash
ls -R
```

Vous devez voir :

```bash
.:
fichier1.txt  fichier2.txt  fichier3.txt  sous-dossier

./sous-dossier:
```

### 2. Ajouter du contenu

Insérer du texte :

```bash
echo "Ceci est un test de contenu dans fichier1.txt" > fichier1.txt
echo -e "ligne1\nligne2\nligne3\nligne4\nligne5" > fichier2.txt
echo -e "apple\nbanana\ncherry\nbanana\napple\nlemon\norange" > fruits.txt
```

### 3. Lire et naviguer dans les fichiers

Afficher tout le contenu :

```bash
cat fichier1.txt
```

Lire page par page :

```bash
less fichier2.txt
```

Appuyer sur `q` pour quitter.

Voir les premières lignes :

```bash
head -n 2 fichier2.txt
```

Voir les dernières lignes :

```bash
tail -n 1 fichier2.txt
```

---

## 🗂️ Copier, déplacer, renommer et supprimer

### 1. Copier et renommer des fichiers

Copier un fichier :

```bash
cp fichier1.txt sous-dossier/fichier1_copie.txt
```

Renommer un fichier :

```bash
mv fichier3.txt fichier3_renomme.txt
```

### 2. Déplacer des fichiers

Déplacer un fichier :

```bash
mv fichier2.txt sous-dossier/
```

Déplacer plusieurs fichiers :

```bash
mv fruits.txt sous-dossier/
```

Vérifiez le contenu :

```bash
ls -R
```

Vous devez voir :

```bash
.:
fichier1.txt  fichier3_renomme.txt  sous-dossier

./sous-dossier:
fichier1_copie.txt  fichier2.txt  fruits.txt
```

### 3. Supprimer fichiers et dossiers

Supprimer un fichier spécifique :

```bash
rm sous-dossier/fichier1_copie.txt
```

Supprimer plusieurs fichiers :

```bash
rm sous-dossier/*
```

Supprimer un dossier vide :

```bash
rmdir sous-dossier
```

Créer puis supprimer un dossier contenant des fichiers :

```bash
mkdir dossier_temp
touch dossier_temp/temp1.txt dossier_temp/temp2.txt
rm -r dossier_temp
```

---

## 🔎 Rechercher et analyser du contenu

### 1. Chercher dans des fichiers

Créer un fichier de test :

```bash
echo -e "apple\nbanana\ncherry\nlemon\norange" > fruits.txt
```

Afficher toutes les lignes contenant "apple" :

```bash
grep apple fruits.txt
```

Rechercher "banana" :

```bash
grep banana fruits.txt
```

Compter les occurrences :

```bash
grep -c apple fruits.txt
```

### 2. Compter lignes, mots, caractères

Compter tout dans un fichier :

```bash
wc fichier1.txt
```

Compter uniquement les lignes :

```bash
wc -l fruits.txt
```

Compter les mots :

```bash
wc -w fruits.txt
```

Compter les caractères :

```bash
wc -c fruits.txt
```

---

## 📑 Analyser des fichiers

### 1. Vérifier le type d'un fichier

Déterminez le type de **fichier1.txt** :

```bash
file mon-premier-dossier/fichier1.txt
```

Testez aussi avec un fichier binaire comme `/bin/ls` :

```bash
file /bin/ls
```

### 2. Afficher les métadonnées d'un fichier

Obtenez toutes les informations sur **fichier3_renomme.txt** :

```bash
stat mon-premier-dossier/fichier3_renomme.txt
```

Observez :

- Taille,
- Dates de création/modification,
- Permissions.

---

## 🧮 Vérifier l'occupation disque

### 1. Taille d'un fichier ou dossier

Affichez la taille d'un seul fichier :

```bash
du -h mon-premier-dossier/fichier1.txt
```

Affichez la taille totale du dossier **mon-premier-dossier** :

```bash
du -sh mon-premier-dossier
```

Détaillez tous les fichiers et sous-dossiers :

```bash
du -h mon-premier-dossier
```

### 2. Espace disque disponible

Visualisez l'espace disque global :

```bash
df -h
```

## 🔍 Recherche de fichiers

### 1. Utiliser `find`

Recherchez tous les fichiers `.txt` dans **mon-premier-dossier** :

```bash
find mon-premier-dossier -name "*.txt"
```

Recherchez tous les fichiers dans **mon-premier-dossier** modifiés il y a moins d'un jour :

```bash
find mon-premier-dossier -mtime -1
```

### 2. Utiliser `locate`

Mettez à jour la base de données `locate` (sur Debian) :

```bash
sudo apt install plocate
```

Recherchez un fichier contenant `fichier1` :

```bash
locate fichier1
```

### 3. Utiliser `which` et `whereis`

Localisez le chemin du binaire `ls` :

```bash
which ls
```

Localisez toutes les informations sur `bash` :

```bash
whereis bash
```

---

## 🛠️ Évaluation avec pytest

Exécuter les tests :

```bash
cd ~/linux-training/tp01-navigation-fichiers
pytest -v
```

Vérifiez que tous les tests passent. Si un test échoue, corrigez votre code.
Voici ce que vous devriez voir :

```bash
--- test session starts ----
platform linux -- Python 3.9.22, pytest-8.3.5, pluggy-1.5.0 -- /home/bob/.pyenv/versions/3.9.22/bin/python3.9
cachedir: .pytest_cache
rootdir: /home/bob/Projets/linux-training/tp-01-navigation-fichiers
plugins: testinfra-10.2.2
collected 4 items

tests/test_tp.py::test_dossier_existe PASSED                                                                                            [ 25%]
tests/test_tp.py::test_fichiers_presents PASSED                                                                                         [ 50%]
tests/test_tp.py::test_contenu_fichier1 PASSED                                                                                          [ 75%]
tests/test_tp.py::test_contenu_fruits PASSED                                                                                            [100%]

------ 4 passed in 0.03s -------
```

---

**À partir du prochain TP** : seules **les actions** seront décrites. Vous devrez chercher **vous-même** comment utiliser les commandes !

