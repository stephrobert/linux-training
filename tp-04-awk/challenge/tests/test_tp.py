import os
import subprocess
import pytest

VENTES_CONTENT = """Produit,Montant
Stylo,2.5
Cahier,4.0
Clé USB,9.99
Clé USB,7.00
Stylo,1.75
"""

EXPECTED_OUTPUT = """Clé USB: 9.99
Clé USB: 7.00
Total: 16.99
"""

def test_script_existence():
    assert os.path.exists("analyse_ventes.awk"), "Le fichier 'analyse_ventes.awk' est manquant."

def test_awk_output(tmp_path):
    ventes_file = tmp_path / "ventes.csv"
    ventes_file.write_text(VENTES_CONTENT)

    result = subprocess.run(
        ["awk", "-f", "analyse_ventes.awk", str(ventes_file)],
        capture_output=True, text=True
    )

    assert result.returncode == 0, f"awk a échoué : {result.stderr}"
    assert result.stdout.strip() == EXPECTED_OUTPUT.strip(), "La sortie n'est pas correcte."
