# TP 08 : Gérer des services

## Introduction

`Systemd` est le gestionnaire de services systèmes de GNU/Linux.  
Il permet d’assurer le démarrage, l’arrêt et l’ordonnancement entre les divers services qui sont
exécutés sur le système.

Il utilise des fichiers descriptifs au format `ini` pour savoir quoi, quand et comment démarrer/arrêter.

Lisez les documentations :
- [Gestion des Services Linux avec systemctl](https://blog.stephane-robert.info/docs/admin-serveurs/linux/services/)
---

## 📚 Résumé de la documentation technique

- **Nom** : `systemctl`
- **Type** : Gestion de services système
- **Fonctionnalités principales** :
    - Connaître l’état d’un service système
    - Arrêt et démarrage de services système
    - Ordonnancement des services (notions de dépendences)

- **Nom** : `journalctl`
- **Type** : Gestion des journaux système
- **Fonctionnalités principales** :
    - Consulter les journaux système
    - Consulter les journaux d’un service système donné

## Prérequis

Pour pouvoir manipuler un service système sans impact sur les services essentiels de la machine, installez `haveged`.

`Haveged` est un générateur d’entropie pour les systèmes Linux.  
Il n’est pas vital au fonctionnement du système, et ne consomme quasiment pas de ressources.  
Son installation permettra de manipuler `systemctl` et `journalctl` sans risquer de causer de problèmes fonctionnels
à votre système.

Pour installer `haveged`, exécuter la commande suivante :

```shell
sudo apt install haveged
```

## Tutoriels

### Exercice 1 : Dans quel état est le service ?

- **Objectif** : Vérifier l’état d’un service géré par `systemd`

**Étapes :**

1. Obtenez les informations sur le service `haveged` :
  ```shell
  systemctl status haveged.service
  ```

2. Vérifiez l’état du service au travers de la ligne `Active:` :
  ```text
  Active: active (running) since ...
  ```


3. Comparez les informations entre l’exécution en utilisateur standard et en root :
  ```test
  systemctl status haveged.service
  sudo systemctl status haveged.service
  ```

4. Arrêtez le service `haveged` avec la commande :
  ```shell
  sudo systemctl stop haveged
  ```

5. Analysez l’état du service. Vous devriez voir la ligne `Active` qui ressemble à cela :
  ```text
  Active: inactive (dead) since ...
  ```

6. Redémarrez le service `haveged` avec la commande :
  ```text
  sudo systemctl start haveged
  ```

- **Commandes utilisées** :
    - `systemctl` : permet d’interrager avec le gestionnaire de service `systemd`

### Exercice 2 : Comment se comporte mon service ?

- **Objectif** : Comprendre comment et quand est démarré un service

**Étapes :**

1. Vérifier l’état au démarrage du système d’un service avec la commande :
  ```shell
  systemctl is-enabled haveged.service
  ```

2. Vérifier les services qui doivent être lancé avant le service que l’on consulte via `systemctl` :
  ```shell
  systemctl list-dependencies --after haveged.service
  ```

3. Vérifier les services qui doivent être lancé après le  service que l’on consulte via `systemctl` :
  ```shell
  systemctl list-dependencies --before haveged.service
  ```

4. Vérifier le contenu de la configuration du service (vérifier les directives `After`, `Before` et `WantedBy`):
  ```shell
  systemctl cat haveged.service
  ```

5. Désactiver un service au démarrage du système avec la commande :
  ```shell
  sudo systemctl disable haveged.service
  ```

6. Vérifier l’état au démarrage du système du service :
  ```shell
  systemctl is-enabled haveged.service
  ```

7. Réactiver le service au démarrage du système :
  ```shell
  systemctl enable haveged.service
  ```

### Exercice 3 : Les journaux d’un service

- **Objectif** : Consulter les journaux d’un service

**Étapes**

1. Consulter les journaux de l’ensemble du système :
  ```shell
  sudo journalctl
  ```

2. Consulter les journaux d’un service
  ```shell
  sudo journalctl -u haveged.service
  ```

- **Commandes utilisées** :
    - `journalctl` : permet l’intéraction avec le service `journald` qui stocket les journaux des différents
      services système

---

## 🏁 Challenge à valider

Consultez le dossier [`challenge/`](./challenge/) pour réaliser un exercice
final permettant de valider vos compétences à l'aide de tests automatisés.