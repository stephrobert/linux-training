# TP 03 : Scripting Shell sous Linux

## Introduction

Ce TP a pour objectif de vous initier à l'écriture de scripts Shell sous Linux.
Vous apprendrez à automatiser des tâches simples, à manipuler des variables, à
utiliser des structures de contrôle, à gérer les entrées/sorties, et à
structurer vos scripts avec des fonctions. Ces compétences sont essentielles
pour les administrateurs système et les développeurs DevOps.

## Résumé de la documentation

- **Shell Bash** : Interpréteur de commandes pour exécuter des scripts.
- **Variables** : Affectation avec `nom="valeur"`, usage via `$nom`.
- **Structures de contrôle** : `if`, `else`, `elif`, `for`, `while`.
- **Fonctions** : Organisation du code en blocs réutilisables.
- **Debug** : `bash -x script.sh`, `set -e`, `set -u`.
- **Bonnes pratiques** : utilisation de `shellcheck`.

Le lien vers la documentation complète est disponible
[ici](https://blog.stephane-robert.info/docs/admin-serveurs/linux/script-shell/).

## Tutoriels

### Exercice 1 : Bonjour, monde !

- **Objectif** : Créer un script `bonjour.sh` qui affiche "Bonjour, monde !".

**Étapes :**

1. Crée un fichier nommé `bonjour.sh` avec la commande suivante :

   ```bash
   nano bonjour.sh
   ```

2. Écris le contenu suivant :

   ```bash
   #!/bin/bash
   echo "Bonjour, monde !"
   ```

3. Rends le script exécutable :

   ```bash
   chmod +x bonjour.sh
   ```

4. Exécute le script :

   ```bash
   ./bonjour.sh
   ```

- **Commandes utilisées** :
  - `echo` : affiche une ligne de texte dans le terminal.
  - `chmod +x` : rend un fichier exécutable.

### Exercice 2 : Bonjour personnalisé

- **Objectif** : Lire un nom au clavier et afficher "Bonjour, <nom> !".

**Étapes :**

1. Crée un fichier `bonjour_perso.sh` :

   ```bash
   nano bonjour_perso.sh
   ```

2. Contenu du script :

   ```bash
   #!/bin/bash
   echo "Quel est votre prénom ?"
   read prenom
   echo "Bonjour, $prenom !"
   ```

3. Rends-le exécutable :

   ```bash
   chmod +x bonjour_perso.sh
   ./bonjour_perso.sh
   ```

### Exercice 3 : Pair ou impair

- **Objectif** : Demander un nombre à l'utilisateur et indiquer s'il est pair ou impair.

**Étapes :**

1. Crée un script `pair_ou_impair.sh` :

   ```bash
   nano pair_ou_impair.sh
   ```

2. Contenu :

   ```bash
   #!/bin/bash
   echo "Entrez un nombre :"
   read nombre
   if [ $((nombre % 2)) -eq 0 ]; then
     echo "$nombre est pair."
   else
     echo "$nombre est impair."
   fi
   ```

3. Rends-le exécutable et teste-le.

### Exercice 4 : Compteur de lignes

- **Objectif** : Créer un script qui lit un fichier texte fourni en argument et affiche son nombre de lignes.

**Étapes :**

1. Crée un script `nb_lignes.sh` :

   ```bash
   nano nb_lignes.sh
   ```

2. Contenu :

   ```bash
   #!/bin/bash
   if [ -f "$1" ]; then
     wc -l "$1"
   else
     echo "Fichier non trouvé."
   fi
   ```

3. Teste avec un fichier texte.

### Exercice 5 : Factorielle

- **Objectif** : Écrire une fonction qui calcule la factorielle d'un nombre donné.

**Étapes :**

1. Crée un script `factorielle.sh` :

   ```bash
   nano factorielle.sh
   ```

2. Contenu :

   ```bash
   #!/bin/bash
   factorielle() {
     n=$1
     resultat=1
     while [ $n -gt 1 ]; do
       resultat=$((resultat * n))
       n=$((n - 1))
     done
     echo $resultat
   }

   echo "Entrez un nombre :"
   read nombre
   factorielle $nombre
   ```

3. Rendez-le exécutable et testez avec divers nombres.

---

## 🏁 Challenge à valider

Consultez le dossier [`challenge/`](./challenge/) pour réaliser un exercice
final permettant de valider vos compétences à l'aide de tests automatisés. Une
fois le challenge terminé, je vous invite à lire mon guide sur [les bonnes
pratiques de développement de scripts
Shell](https://blog.stephane-robert.info/docs/admin-serveurs/linux/scripts-shell-securises/).
