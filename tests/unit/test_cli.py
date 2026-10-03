from sifunapilot import __version__


def test_version():
    assert __version__ == "0.1.0"


def test_cli_import():
    from sifunapilot.cli import main
    assert main is not None
