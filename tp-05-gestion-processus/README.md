# 🖥️ TP : Gestion des Processus sous Linux

## Introduction

Ce TP a pour objectif d'apprendre à gérer les **processus sous Linux**, qui
représentent les programmes en cours d'exécution. Vous apprendrez à surveiller,
contrôler, ajuster la priorité des processus, et à les arrêter proprement ou de
manière forcée.

Ces compétences sont essentielles pour :

* Identifier des processus gourmands en ressources.
* Modifier la priorité d'un processus pour optimiser les performances.
* Arrêter un processus qui pose problème.

🔗 Lien vers la documentation : [Gestion des processus
Linux](https://blog.stephane-robert.info/docs/admin-serveurs/linux/gestion-processus/)

## Résumé de la documentation technique

* **ps** : Lister les processus.
  * Exemple : `ps aux`
* **top** : Surveiller en temps réel les processus.
  * Exemple : `top`
* **htop** : Version améliorée de `top` (si disponible).
* **nice** : Lancer un processus avec une priorité définie.
  * Exemple : `nice -n 10 commande`
* **renice** : Modifier la priorité d’un processus en cours.
  * Exemple : `renice -n 5 -p 1234`
* **kill** : Envoyer un signal à un processus (ex : arrêt).
  * Exemple : `kill -9 1234`
* **killall** : Arrêter tous les processus d’un même nom.
* **pstree** : Visualiser l'arborescence des processus.

## Exercices

### Exercice 1 : Lister tous les processus

* **Objectif** : Lister tous les processus actifs sur votre système.
* **Commande** :

```bash
ps aux
```

**Explication** : Cette commande affiche tous les processus en cours avec des
détails : PID, utilisateur, % CPU, % MEM, etc.

---

### Exercice 2 : Surveiller les processus en temps réel

* **Objectif** : Surveiller la consommation des processus en direct.
* **Commande** :

```bash
top
```

**Explication** : Permet de suivre en temps réel l’état des processus et de
trier par utilisation CPU ou mémoire.

---

### Exercice 3 : Modifier la priorité d'un processus

* **Objectif** : Lancer un script en arrière-plan et modifier sa priorité.
* **Commandes** :

```bash
./fichiers/processus.sh &
pgrep -f processus.sh
```

Récupérer le PID du processus avec `pgrep` et ajuster la priorité :

```bash
renice -n 10 -p [PID]
```

**Explication** : Vous lancez le processus avec `&` puis ajustez sa priorité
avec `renice`. Remplacez `[PID]` par l'identifiant du processus.

On vérifie la priorité avec :

```bash
ps -o pid,ni,comm
```

**Explication** : `ps -o pid,ni,comm` affiche le PID, la priorité et le nom du
processus. `ni` représente la valeur de nice, qui indique la priorité du
processus. Plus la valeur est élevée, moins le processus est prioritaire.
Vous pouvez également utiliser `htop` pour visualiser les processus et leur
priorité de manière graphique.

---

### Exercice 4 : Tuer un processus

* **Objectif** : Tuer le processus créé précédement.
* **Commandes** :

```bash
kill -9 [PID]
```

**Explication** : `kill -9` envoie le signal SIGKILL pour forcer la terminaison
immédiate du processus.

---

### Exercice 5 : Suspendre et reprendre un processus

* **Objectif** : Tester la suspension et la reprise d’un processus.
* **Commandes** :

```bash
./fichiers/processus.sh
```

On vient de lancer le script `processus.sh` en avant-plan. Pour le
suspendre, utilisez `Ctrl + Z`. Cela met le processus en pause.

Pour visualiser les processus suspendus, utilisez :

```bash
jobs
```

**Explication** : `jobs` affiche la liste des jobs en arrière-plan. Le
processus suspendu sera marqué comme "Stopped".

Pour le reprendre, utilisez la commande `bg` :

```bash
bg %1
```

**Explication** : `bg %1` reprend le processus en arrière-plan. Vous pouvez
également le ramener au premier plan avec `fg %1`.

Tuons les processus en arrière-plan avec :

```bash
pgrep -f processus.sh

kill -9 %[PID]
```

---

## 🚩 Challenge à valider

Rendez-vous dans le dossier [`challenge/`](./challenge/README.md) pour découvrir
et réaliser le challenge final 🎯 !

