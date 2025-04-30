# 🎯 Challenge final : Analyse automatique d’un fichier CSV d’utilisateurs

## 📝 Objectif

Vous devez créer un script **`analyse_utilisateurs.sh`** qui effectue plusieurs
traitements sur un fichier CSV `utilisateurs.csv`. Chaque ligne du fichier est
structurée ainsi :

```csv
nom,age
Alice,22
Bob,35
Charlie,17
```

---

## ✅ Étapes à implémenter dans le script

1. **Vérifier l’existence du fichier `utilisateurs.csv`**. S’il est manquant,
   afficher un message d’erreur et quitter avec un code différent de 0.
2. **Compter le nombre total d’utilisateurs** et l’afficher.
3. **Calculer et afficher l’âge moyen**.
4. **Lister les utilisateurs majeurs (âge ≥ 18)** dans un fichier `majeurs.txt`.
5. **Afficher le nom de l’utilisateur le plus âgé.**

---

## ⚙️ Contraintes

- Le script ne doit utiliser **aucune commande externe avancée** comme `awk`,
  `jq`, `python`, etc. : utilisez uniquement Bash, `read`, `cut`, `expr`, `if`,
  `while`, etc.

---

## 📦 À rendre

- Le fichier `resultats.txt` (à créer)
- `majeurs.txt` (généré automatiquement)
- Le fichier `utilisateurs.csv` (sera fourni dans le test)

---

## ▶️ Lancer les tests

Depuis le dossier `challenge/` :

```bash
pytest -v
```

Si tous les tests passent, le challenge est validé.

```plaintext
=== test session starts ===
platform linux -- Python 3.9.22, pytest-8.3.5, pluggy-1.5.0 -- /home/bob/.pyenv/versions/3.9.22/bin/python3.9
cachedir: .pytest_cache
rootdir: /home/bob/Projets/linux-training/tp-03-premiers-scripts-shell/challenge
plugins: testinfra-10.2.2

collected 5 items

tests/test_tp.py::test_script_existe[local] PASSED        [ 20%]
tests/test_tp.py::test_script_executable[local] PASSED    [ 40%]
tests/test_tp.py::test_sortie_terminal[local] PASSED      [ 60%]
tests/test_tp.py::test_majeurs_txt[local] PASSED          [ 80%]
tests/test_tp.py::test_utilisateur_plus_age[local] PASSED [100%]

==== 5 passed in 0.20s ====
```
