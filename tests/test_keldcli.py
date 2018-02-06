# -*- coding: utf-8 -*-

from click.testing import CliRunner

from keldcli import cli


def test_cli():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code == 0


def test_keldcli_as_module():
    import subprocess
    returncode = subprocess.call(['python', '-m', 'keldcli'])
    assert(returncode == 0)


def test_keldcli_as_script():
    import subprocess
    returncode = subprocess.call(['keld'])
    assert(returncode == 0)
