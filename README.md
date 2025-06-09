# TP Linux pour Administrateurs Systèmes

Bienvenue dans ce projet de **Travaux Pratiques Linux** !

Ces TP vous guideront dans l'apprentissage pratique de l'**administration
système Linux**. Chaque TP est organisé dans un **sous-dossier** avec son propre
énoncé. Au début, les explications seront détaillées, mais très vite, vous serez
plus autonome dans l'exécution des tâches demandées.

## Pré-requis

### Environnement

- Une machine (ou wsl2 pour ceux qui sont sous windows) avec une distribution
  **Debian** ou une de ses dérivées fraîchement installée (par exemple Debian
  12).
- **Accès administrateur (root)** ou un utilisateur pouvant utiliser `sudo`.
- **Virtualisation activée** dans le BIOS/UEFI (Intel VT-x ou AMD-V), car
  certains TP utiliseront la **virtualisation** pour manipuler d'autres
  distributions Linux.

**Conseil :** vérifiez si la virtualisation est activée :

```bash
egrep -c '(vmx|svm)' /proc/cpuinfo
```

Un résultat supérieur à 0 indique que la virtualisation est active.

### Logiciels

- Installer **Python 3** et **pip** :

```bash
sudo apt update
sudo apt install python3 python3-pip
```

- Installer **pytest** et **testinfra** pour valider vos exercices :

```bash
pip install pipx --user
pipx install pytest
pipx inject pytest pytest-testinfra
```

- Cloner ce dépôt :

```bash
git clone <URL_DU_DEPOT>
cd <nom_du_dossier>
```

**Vérifications rapides :**

```bash
python3 --version
pytest --version
```

A partir du TP 7, il sera nécessaire d'installer **Incus** (anciennement LXD).
En effet, Incus est un gestionnaire de conteneurs et de machines virtuelles qui
vous permet de créer et gérer des environnements virtuels. Il est
particulièrement utile pour les TP qui risquent d'endommager votre instance de Linux.

Pour l'installer, exécutez les commandes suivantes :

```bash
sudo apt install incus
```

Initialiser Incus :

```bash
sudo incus init --minimal
```

## Documentation obligatoire

Avant de commencer un TP, vous devez **lire la documentation** liée au sujet sur
[mon site de documentation Linux](https://blog.stephane-robert.info/docs/).

Chaque énoncé précisera quelle section lire.
**Aucune aide ne sera donnée sur des notions qui y sont expliquées.**

**Exemples de lectures recommandées :**

- [Introduction aux Serveurs
  Linux](https://blog.stephane-robert.info/docs/admin-serveurs/linux/)
- [Apprendre les commandes Linux de
  base](https://blog.stephane-robert.info/docs/admin-serveurs/linux/commandes/)

## Structure du projet

Chaque TP est placé dans un **sous-dossier** indépendant :

```bash
/Linux-training/
│
├── tp01-navigation-fichiers/
│   └── README.md
│   └── challenge/
│       ├── README.md
│       └── tests/
│           └── test_tp.py
├── tp-02-commandes-avancees/
│   └── README.md
│   └── challenge/
│       ├── README.md
│       └── tests/
│           └── test_tp.py
├── ...
```

Chaque sous-dossier contient :

- Un fichier `README.md` avec les consignes.
- Un dossier `challenge/` avec :
  - Un fichier `README.md` avec les consignes.
  - Un dossier tests contenant un fichier `test_tp.py` pour valider automatiquement votre travail.

## Comment travailler sur un TP

1. Lire la documentation liée au sujet sur [le
   site](https://blog.stephane-robert.info/docs/).
2. Lire attentivement le `README.md` contenu dans le dossier du TP.
3. Effectuer les tâches demandées dans votre terminal.
4. Relever le challenge dans le dossier `challenge/` :
5. Vérifier votre travail avec **pytest** :

```bash
pytest -v
```

Les tests vous indiqueront si votre solution est correcte.

## Important

- **Aucune réponse n’est donnée** dans les énoncés après les premiers TP.
- **Cherchez par vous-même** avec l'aide des commandes Linux (`--help`, `man`,
  etc.).
- **Validez vos résultats** uniquement via les tests automatisés.
- **Si vous bloquez**, n'hésitez pas à demander de l'aide sur
  [le discord](https://blog.stephane-robert.info/docs/discord/).

## Mise à jour du dépôt

Je vais continuer à mettre à jour ce dépôt avec de nouveaux exercices et des
améliorations. Pour récupérer les dernières modifications, vous pouvez
simplement exécuter :

```bash
git pull origin main
```

## Contribuer

Bien entendu, vous êtes invités à contribuer à ce dépôt en proposant des
améliorations ou en corrigeant des erreurs. N'hésitez pas à ouvrir une **issue**
ou à soumettre une **pull request**.

Plus d'infos [ici](https://github.com/stephrobert/containers-training/blob/main/contributing.md)

## Me soutenir

Si vous appréciez ce travail et souhaitez me soutenir, vous pouvez me payer un
café ☕️:

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/stephanerobert89902)

## Copyright et licence

Tous les contenus contenus dans ce repo sont :

- Copyright ©2025 Stéphane Robert
- Distribués sous [licence Creative Commons BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

![Creative Commons BY-SA](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-sa.png)
