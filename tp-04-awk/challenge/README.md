# 🏁 Challenge final : Traitement de données CSV avec `awk`

## 🎯 Objectif

Vous devez écrire un script `awk` nommé `analyse_ventes.awk` qui lit un fichier
CSV nommé `ventes.csv` (séparé par des virgules) contenant des enregistrements
de ventes sous la forme :

```csv
Produit,Montant
Stylo,2.5
Cahier,4.0
Clé USB,9.99
Clé USB,7.00
Stylo,1.75
```

Le script devra :

1. **Afficher uniquement les lignes contenant le mot "Clé USB"** ;
2. **Afficher uniquement le montant de ces ventes** ;
3. **Calculer le total des montants pour "Clé USB"**.

## 💡 Format attendu de la sortie

```bash
Clé USB: 9.99
Clé USB: 7.00
Total: 16.99
```

## 🛠️ Consignes

- Le script doit s'appeler `analyse_ventes.awk` ;
- Il doit fonctionner avec la commande suivante :

  ```bash
  awk -f analyse_ventes.awk fichiers/ventes.csv
  ```

## ✅ Critères de validation

Le challenge est validé automatiquement si les tests passent avec succès :

```bash
pytest -v
```

Exemple de sortie :

```plaintext
=== test session starts ====
platform linux -- Python 3.9.22, pytest-8.3.5, pluggy-1.5.0 -- /home/bob/.pyenv/versions/3.9.22/bin/python3.9
cachedir: .pytest_cache
rootdir: /home/bob/Projets/linux-training/tp-04-awk/challenge
plugins: testinfra-10.2.2
collected 2 items

tests/test_tp.py::test_script_existence PASSED     [ 50%]
tests/test_tp.py::test_awk_output PASSED           [100%]

==== 2 passed in 0.04s =====
```
