
# 🎯 Challenge Final : Maîtriser `xargs`

**Objectif :** Supprimer tous les fichiers `.txt` présents dans le dossier `../fichiers/` en utilisant `xargs` de manière sécurisée (en tenant compte des espaces dans les noms de fichiers).

## Consignes :

- Utilisez `find` avec `-print0` et `xargs -0` pour traiter les noms avec des espaces.
- Lancez la commande depuis la racine du projet (à côté du dossier `challenge/`).

✅ Pour vérifier votre travail :

```bash
pytest challenge/tests/
```
