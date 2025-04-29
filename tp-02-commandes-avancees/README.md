# TP 2 : Maîtriser les Commandes Avancées de Linux

## Objectif

Apprendre à :

- Surveiller les **ressources système**,
- Gérer les **processus**,
- Manipuler, trier et transformer des **données texte**,
- Automatiser des traitements avec des **scripts shell**.

**Remarque** : Ce TP est en partie guidé. Dans la partie 3, **vous devrez vous
débrouillez seul**. Donc n'hésitez pas à vous poser des questions pour essayer
de comprendre ce qui se passe.

## Prérequis

- Avoir lu la documentation sur les commandes de
  [base](https://blog.stephane-robert.info/docs/admin-serveurs/linux/commandes/)
  et
  [avancées](https://blog.stephane-robert.info/docs/admin-serveurs/linux/commandes-avancees/).

---

## 📁 Préparation de l'environnement

Placez-vous dans le répertoire de travail :

```bash
cd ~/linux-training/tp-02-commandes-avancees
```

Créez un nouveau dossier de travail :

```bash
mkdir mon-second-dossier
cd mon-second-dossier
mkdir data
cd data
```

Créez les fichiers suivants :

```bash
seq 1 100 > nombres.txt
yes "ligne identique" | head -n 10 > lignes.txt
echo -e "apple\nbanana\napple\ncherry\nbanana\ncherry\napple" > fruits.txt
```

---

## 🏁 Partie 1 : Analyse système (guidée)

### 1. Occupation disque

```bash
df -h
du -sh .
du -h nombres.txt
```

### 2. Utilisation mémoire et charge

```bash
free -h
uptime
```

### 3. Observer les processus

```bash
ps aux | head -n 10
top
```

Pour quitter `top`, appuyez sur `q`.

Lancez un processus de test :

```bash
yes > /dev/null &
```

Trouvez son PID :

```bash
ps aux | grep "yes"
```

Arrêtez-le :

```bash
kill <PID>
```

---

## 🔧 Partie 2 : Manipulations de fichiers texte (guidée)

### 1. Encadrer chaque ligne de `nombres.txt` avec des crochets

```bash
cat nombres.txt | xargs -n 1 | sed 's/^/[/' | sed 's/$/]/' > nombres_formates.txt
```

### 2. Extraire les 3 premières lettres de chaque ligne de `fruits.txt`

```bash
cut -c 1-3 fruits.txt > fruits_cut.txt
```

### 3. Trier et supprimer les doublons

```bash
sort fruits.txt > fruits_tries.txt
uniq fruits_tries.txt > fruits_uniques.txt
```

### 4. Compter les occurrences

```bash
sort fruits.txt | uniq -c > fruits_stats.txt
```

### 5. Afficher et enregistrer en même temps

```bash
sort fruits.txt | tee fruits_output.txt
```

---

## 🧩 Partie 3 — Manipulations de fichiers (consignes simplifiées)

> **But** : produire des fichiers de résultats. Vous devez deviner les commandes
> à utiliser en vous aidant de `man`, `tldr` ou `--help`.

1. Créez un fichier `crochets.txt` contenant les nombres de `nombres.txt`
   entourés de `[]` (exemple : `[1]`, `[2]`, etc.). Utilisez la commande sed !

2. Dans `fruits.txt`, récupérez les **3 premières lettres** de chaque mot et
   enregistrez-les dans `debut_fruits.txt`.

3. Triez les lignes de `fruits.txt` par ordre alphabétique dans un fichier
   `fruits_tries.txt`. Utilisez `sort`.

4. Supprimez les doublons et enregistrez le résultat dans `fruits_uniques.txt`.

5. Comptez combien de fois chaque fruit apparaît et enregistrez dans
   `compte_fruits.txt`. Utilisez `sort` et `uniq`.

6. Ajoutez un horodatage dans un fichier `journal_execution.txt`.

---

## 🛠️ Évaluation avec pytest

Exécuter les tests :

```bash
cd ../..
pytest -v
```

Vous devez voir un message indiquant que tous les tests sont passés. Si ce n'est pas
le cas, corrigez votre code.

```bash
❯ pytest -v
============================================================= test session starts =============================================================
platform linux -- Python 3.9.22, pytest-8.3.5, pluggy-1.5.0 -- /home/bob/.pyenv/versions/3.9.22/bin/python3.9
cachedir: .pytest_cache
rootdir: /home/bob/Projets/linux-training/tp-02-commandes-avancees
plugins: testinfra-10.2.2
collected 6 items

tests/test_tp.py::test_crochets_format PASSED                                                                                           [ 16%]
tests/test_tp.py::test_debut_fruits PASSED                                                                                              [ 33%]
tests/test_tp.py::test_fruits_tries PASSED                                                                                              [ 50%]
tests/test_tp.py::test_fruits_uniques PASSED                                                                                            [ 66%]
tests/test_tp.py::test_compte_fruits PASSED                                                                                             [ 83%]
tests/test_tp.py::test_journal_execution PASSED                                                                                         [100%]

======== 6 passed in 0.04s ========


