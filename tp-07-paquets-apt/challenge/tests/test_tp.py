import testinfra

def test_sources_list(host):
    sources = host.file("/etc/apt/sources.list")
    assert sources.exists
    assert sources.contains("deb http://deb.debian.org/debian buster main")

def test_preferences(host):
    preferences = host.file("/etc/apt/preferences")
    assert preferences.exists
    assert preferences.contains("Package: nano")
    assert preferences.contains("Pin: version 7.2")
    assert preferences.contains("Pin-Priority: 1001")

def test_nano_version(host):
    nano = host.package("nano")
    assert nano.is_installed
    assert nano.version == "7.2"
