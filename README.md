# TP Linux pour Administrateurs Systèmes

Bienvenue dans ce projet de **Travaux Pratiques Linux** !

Ces TP vous guideront dans l'apprentissage pratique de l'**administration
système Linux**. Chaque TP est organisé dans un **sous-dossier** avec son propre
énoncé. Au début, les explications seront détaillées, mais très vite, vous serez
plus autonome dans l'exécution des tâches demandées.

## Pré-requis

### Environnement

- Une machine physique avec une distribution **Debian** ou une de ses dérivées
  fraîchement installée (par exemple Debian 12).
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
pip3 install -r requirements.txt
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