# -*- coding: utf-8 -*-

"""Test the invokation of the `keldcli` package."""


def test_keldcli_as_module():
    """Test that the package can be run as a module (`python -m keldcli`)."""
    import subprocess
    returncode = subprocess.call(['python', '-m', 'keldcli'])
    assert returncode == 0


def test_keldcli_as_script():
    """Test the package console script has been installed."""
    import subprocess
    returncode = subprocess.call(['keldcli'])
    assert returncode == 0
