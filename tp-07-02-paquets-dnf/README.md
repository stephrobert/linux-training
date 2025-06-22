# 🖥️ TP : Maîtrisez le gestionnaire de paquets DNF

## Introduction

Ce TP vous apprendra à utiliser **DNF**, le gestionnaire de paquets moderne pour
les distributions Linux basées sur RPM telles que Fedora, RHEL, AlmaLinux ou
Rocky Linux.

L'objectif est d'être capable de :

* Installer, mettre à jour et supprimer des paquets
* Rechercher des logiciels
* Gérer les dépôts et groupes de paquets
* Automatiser la maintenance du système

## Pré-requis

Il faut installer **Incus** sur votre mahcine pour ce TP. La procédure
d'installation est décrite dans le fichier [README.md du
projet](https://github.com/stephrobert/linux-training/blob/main/README.md).

Une fois Incus installé, vous pouvez créer une machine virtuelle Ubuntu 24.04
avec les commandes suivantes depuis le dossier racine du projet `linux-training`
:

```bash
incus launch images:rockylinux/9/cloud rocky  --config=cloud-init.user-data="$(cat cloud-config.yaml)"
incus alias add login 'exec @ARGS@ -- su -l admin'
incus config device add tp mysharedfolder disk source=$PWD path=/home/ubuntu/linux-training shift=true
```

La première commande crée une instance Ubuntu 24.04 sur laquelle sont installés
les packages nécessaires au lancement des tests. La seconde commande permet de
créer un alias pour se connecter facilement à l'instance. La troisième permet de
partager le dossier `linux-training` de votre machine hôte avec l'instance.

Pour vous connecter à la machine virtuelle, utilisez :

```bash
incus login rocky
```

On va installer les paquets python nécessaires pour le bon
fonctionnement des tests :

```bash
cd /home/ubuntu/linux-training/
./install.sh
```

## Résumé de la documentation technique

* `dnf install <paquet>` : installe un paquet
* `dnf remove <paquet>` : supprime un paquet
* `dnf update` : met à jour tous les paquets
* `dnf search <mot_clé>` : recherche un paquet
* `dnf provides <chemin>` : trouve le paquet fournissant un fichier
* `dnf group list/install/remove/info` : gère les groupes de paquets
* `dnf config-manager` : active/désactive un dépôt
* `dnf clean all/metadata/packages` : nettoyage du cache
* `dnf history`, `dnf downgrade`, `dnf reinstall` : commandes avancées
* `dnf-automatic` : outil d'automatisation des mises à jour

👉 Documentation complète :
[https://blog.stephane-robert.info/docs/admin-serveurs/linux/dnf/](https://blog.stephane-robert.info/docs/admin-serveurs/linux/dnf/)

---

## Exercices

### Exercice 1 : Installation d'un paquet

**Objectif :** Installer un serveur HTTP pour la suite du TP.

```bash
dnf install httpd
```

**Explication :** `dnf install` télécharge et installe le paquet spécifié ainsi
que ses dépendances.

### Exercice 2 : Recherche et info

**Objectif :** Trouver un paquet et obtenir ses détails.

```bash
dnf search nano
dnf info nano
```

**Explication :** `search` explore les noms/descriptions ; `info` affiche les
détails d'un paquet.

### Exercice 3 : Mises à jour sélectives

**Objectif :** Mettre à jour un paquet spécifique et exclure le noyau.

```bash
dnf update nano
dnf --exclude=kernel* update
```

**Explication :** `--exclude` empêche certains paquets d'être mis à jour.

### Exercice 4 : Groupes de paquets

**Objectif :** Installer un environnement serveur.

```bash
dnf group list
dnf group install "Web Server"
dnf group info "Web Server"
```

**Explication :** Les groupes regroupent des paquets selon une fonctionnalité
commune.

### Exercice 5 : Nettoyage et résolution

**Objectif :** Nettoyer et réinstaller un paquet.

```bash
dnf clean all
dnf reinstall bash
dnf history
```

**Explication :** `clean all` supprime le cache ; `reinstall` remplace les
fichiers du paquet.

---

## Challenge à valider

Voir [le dossier challenge](./challenge/README.md) pour les consignes finales et
les tests à réussir avec `pytest` et `testinfra`.

Bonne pratique !
