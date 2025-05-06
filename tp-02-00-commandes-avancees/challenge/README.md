# 🎯 Challenge final : Analyse de rapports d'utilisateurs

## 📝 Objectif

À l’aide **exclusivement de commandes Linux**, vous devez effectuer une série de
traitements sur un fichier `utilisateurs.csv` fourni.

🚫 Aucun script ne doit être écrit.
✅ Chaque étape doit produire un fichier de résultat nommé `resultat1.txt`,
`resultat2.txt`, ..., `resultat5.txt`.

---

## ✅ Étapes à effectuer

1. **Extraire la colonne des noms** avec `cut` et la convertir en majuscules
   avec `tr`.
   🔄 Résultat : `resultat1.txt`

2. **Extraire la colonne des âges et remplacer `30` par `31`** avec `cut` +
   `sed`.
   🔄 Résultat : `resultat2.txt`

3. **Fusionner les deux fichiers précédents** avec `paste` pour obtenir
   `NOM,AGE`.
   🔄 Résultat : `resultat3.txt`

4. **Filtrer les utilisateurs âgés de plus de 30 ans** avec `awk`.
   🔄 Résultat : `resultat4.txt`

5. **Numéroter les lignes filtrées** avec `nl`.
   🔄 Résultat : `resultat5.txt`

---

## 📦 À rendre

Les fichiers suivants **doivent exister** :

- `resultat1.txt`
- `resultat2.txt`
- `resultat3.txt`
- `resultat4.txt`
- `resultat5.txt`

---

## ▶️ Lancer les tests

```bash
pytest -v
```

Tous les tests doivent passer pour valider le challenge.

```plaintext
=== test session starts ===
platform linux -- Python 3.9.22, pytest-8.3.5, pluggy-1.5.0 -- /home/bob/.pyenv/versions/3.9.22/bin/python3.9
cachedir: .pytest_cache
rootdir: /home/bob/Projets/linux-training/tp-02-commandes-avancees/challenge
plugins: testinfra-10.2.2
collected 6 items

tests/test_tp.py::test_resultat1_existe_et_non_vide[local] PASSED                                                                                                            [ 16%]
tests/test_tp.py::test_resultat2_existe_et_non_vide[local] PASSED                                                                                                            [ 33%]
tests/test_tp.py::test_resultat3_existe_et_non_vide[local] PASSED                                                                                                            [ 50%]
tests/test_tp.py::test_resultat4_existe_et_non_vide[local] PASSED                                                                                                            [ 66%]
tests/test_tp.py::test_resultat5_existe_et_non_vide[local] PASSED                                                                                                            [ 83%]
tests/test_tp.py::test_resultat5_contenu[local] PASSED                                                                                                                       [100%]

=== 6 passed in 0.19s ===
```
