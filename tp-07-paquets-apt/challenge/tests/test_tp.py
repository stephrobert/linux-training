import testinfra

def test_preferences(host):
    preferences = host.file("/etc/apt/preferences.d/nano")
    assert preferences.exists
    assert preferences.contains("Package: nano")
    assert preferences.contains("Pin: version 7.2*")
    assert preferences.contains("Pin-Priority: 1001")

def test_nano_version(host):
    nano = host.package("nano")
    assert nano.is_installed
    assert nano.version.startswith("7.2")
