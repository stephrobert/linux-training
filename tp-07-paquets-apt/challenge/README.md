# 🧩 Challenge : Installation d'une version fixée d'un package

## 🎯 Objectif

Configurer un système Debian pour qu'il utilise un dépôt spécifique et installe
une version précise d'un paquet, en respectant des préférences définies.

## 📋 Instructions

1. Modifier le fichier `/etc/apt/sources.list` pour ajouter le dépôt suivant :

   ```bash
   deb http://deb.debian.org/debian buster main
   ```

2. Créer ou modifier le fichier `/etc/apt/preferences.d/nano` pour que le paquet `nano`
   soit installé en version `7.2-2` avec une priorité de `1001`.

3. Mettez à jour la liste des paquets et installez nano.


### ✅ Validation

Exécutez les tests avec la commande suivante :

```bash
cd tp-07-paquets-apt
pytest -v challenge/tests/test_tp.py
```

Ce TP vous permettra de maîtriser les bases de la gestion des paquets avec APT
sur Debian et ses dérivés. N'hésitez pas à explorer davantage les
fonctionnalités avancées d'APT pour approfondir vos compétences.
