import testinfra


def test_script_existe_et_non_vide(host):
    f = host.file("systemd-unit-script.sh")
    assert f.exists, "systemd-unit-script.sh n'existe pas"
    assert f.size > 0, "systemd-unit-script.sh est vide"


def test_systemd_unit_existe_et_non_vide(host):
    f = host.file("/etc/systemd/system/mytest-unit.service")
    assert f.exists, "/etc/systemd/system/mytest-unit.service n'existe pas"
    assert f.size > 0, "/etc/systemd/system/mytest-unit.service est vide"


def test_systemd_unit_existe_et_est_valide(host):
    f = host.service("mytest-unit")
    assert f.exists, "Le service mytest-unit.service n'existe pas"
    assert f.is_valid, "Le service mytest-unit.service n’est pas valide"
    assert f.systemd_properties[
        "After"
    ], "Le service mytest-unit.service ne contient pas de directive After"
    assert (
        "haveged.service" in f.systemd_properties["After"]
    ), "Le service mytest-unit.service n’est pas dépendent du service haveged"


def test_systemd_unit_et_demarre(host):
    f = host.service("mytest-unit")
    assert f.is_running, "Le service mytest-unit.service n'est pas demarre"


def test_systemd_unit_et_actif_au_boot(host):
    f = host.service("mytest-unit")
    assert f.is_enabled, "Le service mytest-unit.service n'est pas actif au boot"


def test_unit_logs_output(host):
    logs = host.run("sudo journalctl -u mytest-unit.service")
    assert (
        "Executed" in logs.stdout
    ), "Les journaux du service mytest-unit.service ne sont pas corrects"
