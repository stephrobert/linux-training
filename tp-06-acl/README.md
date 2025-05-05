# TP : Gestion des ACL sous Linux

## Introduction

Ce TP a pour objectif d'apprendre à gérer les **listes de contrôle d'accès
(ACL)** sous Linux, qui permettent de définir des permissions d'accès plus
granulaires que les simples modes `rwx` classiques. Vous apprendrez à consulter
et modifier les ACL à l'aide des commandes principales `getfacl` et `setfacl`.

Les ACL sont très utiles pour :

* Donner des droits spécifiques à certains utilisateurs ou groupes sans changer
  le propriétaire.
* Gérer des cas complexes où les permissions standards sont insuffisantes.

Le lien vers la documentation : [Les ACL
Linux](https://blog.stephane-robert.info/docs/admin-serveurs/linux/acl/)

## Résumé de la documentation technique

* **getfacl** : Permet d'afficher les ACL d'un fichier ou répertoire.

  * Exemple : `getfacl fichier.txt`
* **setfacl** : Permet de définir ou modifier les ACL.

  * Exemple : `setfacl -m u:alice:r fichier.txt` (donne le droit lecture à
    l'utilisateur `alice`)
* **Options utiles** :

  * `-m` : modifier une ACL
  * `-x` : supprimer une ACL
  * `-b` : supprimer toutes les ACL d'un fichier
  * `-R` : appliquer de manière récursive
* **Principe** :

  * Une ACL classique : `user:alice:r--`
  * Pour les répertoires : ne pas oublier la propagation des ACL avec `d:` (ACL
    par défaut)

## Exercices

### Exercice 1 : Vérifier les ACL existantes

* **Fichier** : `fichiers/document1.txt`
* **Objectif** : Affichez les ACL actuelles de ce fichier.
* **Commande** :

```bash
getfacl fichiers/document1.txt
```

**Explication** : Cette commande montre les permissions standards **et** toute
ACL appliquée au fichier.

---

### Exercice 2 : Ajouter un utilisateur

Pour les exercices suivants, vous devez créer un utilisateur `etudiant` et un
groupe `stagiaires` sur votre machine. Vous pouvez le faire avec les commandes
suivantes :

```bash
sudo useradd etudiant
sudo groupadd stagiaires
sudo usermod -aG stagiaires etudiant
```

Nous verrons dans un autre TP comment gérer les utilisateurs et groupes de
manière plus avancée.

### Exercice 3 : Ajouter une permission pour un utilisateur

* **Fichier** : `fichiers/document2.txt`
* **Objectif** : Donnez le droit de lecture à l’utilisateur `etudiant`.
* **Commande** :

```bash
setfacl -m u:etudiant:r fichiers/document2.txt
```

**Explication** : `-m` indique la modification d'ACL, `u:etudiant:r` signifie
qu'on donne le droit lecture à `etudiant`.

---

### Exercice 4 : Ajouter une permission pour un groupe

* **Fichier** : `fichiers/document3.txt`
* **Objectif** : Donnez les droits de lecture et écriture au groupe
  `stagiaires`.
* **Commande** :

```bash
setfacl -m g:stagiaires:rw fichiers/document3.txt
```

**Explication** : `g:stagiaires:rw` cible le groupe `stagiaires` avec les droits
`rw`.

Vérifier les permissions avec :

```bash
getfacl fichiers/document3.txt
```

---

### Exercice 4 : Supprimer une ACL

* **Fichier** : `fichiers/document4.txt`
* **Objectif** : Supprimez l’ACL spécifique pour l’utilisateur `etudiant`.
* **Commande** :

```bash
setfacl -x u:etudiant fichiers/document2.txt
```

**Explication** : `-x` permet de retirer une entrée ACL précise.

---

### Exercice 5 : Appliquer des ACL par défaut à un répertoire

* **Répertoire** : `fichiers/partage/`
* **Objectif** : Assurez-vous que tous les nouveaux fichiers créés dans ce
  dossier donnent lecture/écriture au groupe `stagiaires`.
* **Commande** :

```bash
setfacl -d -m g:stagiaires:rw fichiers/partage/
```

**Explication** : Le `-d` applique une ACL par défaut, utile pour les futurs
fichiers.

Créez un fichier dans le répertoire `fichiers/partage/` pour vérifier que
l'ACL par défaut fonctionne :

```bash
touch fichiers/partage/nouveau_fichier.txt
getfacl fichiers/partage/nouveau_fichier.txt
```

**Explication** : Vérifiez que le groupe `stagiaires` a bien les droits
lecture/écriture sur le nouveau fichier créé.

---

## 🚩 Challenge à valider

Rendez-vous dans le dossier [`challenge/`](./challenge/README.md) pour découvrir
et réaliser le challenge final !

