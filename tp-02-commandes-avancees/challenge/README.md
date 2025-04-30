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
