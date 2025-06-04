# 🎯 Challenge final : Créer une configuration de service système

## 📝 Objectif


---

## ✅ Étapes à effectuer

1. **Créer un script qui sera exécuté en service système** : Le script va simplement afficher des lignes à l’aide de la commande `echo`
2. **Créer une configuration systemd**
3. **Activer le service au démarrage après un autre service**

---

## ⚙️ Contraintes

- Le script ne doit utiliser **que les commandes basiques** `echo`, `date`, `while` et `sleep`
- Le script doit afficher une ligne au format `Executed at <date> : <sortie du echo>` toutes les 10 secondes

---

## 📦 À rendre

- Un script `systemd-unit-script.sh` (à créer).
- Une configuration systemd `mytest-unit.service` au niveau système.
    - Le service doit démarrer après le service `haveged`.
    - Le service doit démarrer dans le contexte `multi-user`

---

## ▶️ Lancer les tests

Depuis le dossier `challenge/` :

```bash
pytest -v
```

---

## 🚫 Faire le ménage

1. Arrêter votre service système
2. Désactiver votre service système au démarrage