# Autoformation Linux

Pour cette autoformation, nous allons créer une machine virtuelle avec Vagrant. Les tests seront réalisés sur cette machine virtuelle avec Ansible. L'objectif est de créer un environnement de test reproductible et facilement configurable.

## Création de la machine virtuelle

Afin de créer une machine virtuelle, nous allons utiliser Vagrant. Vagrant est un outil de gestion de machines virtuelles qui permet de créer et de configurer des environnements de développement reproductibles.

### Prérequis

- Installer Vagrant
- Installer Libvirt
- Installer Ansible

### Créatio

## Lab 1 : Création d'un fichier

### Objectif

L'objectif de ce lab est de vérifier la création d'un fichier `test.txt` dans le répertoire `/home/vagrant` de la vm créer avec vagrant.

### Consigne

1. Créez un fichier appelé `test.txt` dans `/home/vagrant`.
2. Le contenu du fichier doit être : `Ce fichier a été créé pour le test.`

### Pour valider le lab :

Lancer la commande suivante :

```bash
make test1
```

Si le playbook s'est bien exécuté, vous devriez ne pas avoir d'erreur.