
import pytest

def test_txt_files_deleted(host):
    result = host.run("find ../fichiers/ -name '*.txt'")
    assert result.stdout.strip() == '', "Des fichiers .txt existent encore dans le dossier fichiers/"
