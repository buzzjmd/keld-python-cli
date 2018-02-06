# -*- coding: utf-8 -*-

from keldcli import cli


def test_cli(runner):
    """Test the CLI."""
    result = runner.invoke(cli)
    assert result.exit_code == 0
    assert 'Keld Command Line Interface!\n' in result.output


def test_keldcli_as_module():
    import subprocess
    returncode = subprocess.call(['python', '-m', 'keldcli'])
    assert(returncode == 0)


def test_keldcli_as_script():
    import subprocess
    returncode = subprocess.call(['keld'])
    assert(returncode == 0)


def test_help_option(runner):
    """Test the --help option."""
    help_result = runner.invoke(cli, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
