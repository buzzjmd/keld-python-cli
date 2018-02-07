# -*- coding: utf-8 -*-

"""Tests for the Command Line Interface of the `keldcli` package."""

from keldcli import cli


def test_cli(runner):
    """Test the CLI."""
    result = runner.invoke(cli)
    assert result.exit_code == 0
    assert 'Keld Command Line Interface!\n' in result.output


def test_keldcli_as_module():
    """Test that the package can be run as a module (`python -m keldcli`)."""
    import subprocess
    returncode = subprocess.call(['python', '-m', 'keldcli'])
    assert(returncode == 0)


def test_keldcli_as_script():
    """Test the package script has been installed."""
    import subprocess
    returncode = subprocess.call(['keld'])
    assert(returncode == 0)


def test_help_option(runner):
    """Test the --help option."""
    help_result = runner.invoke(cli, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
