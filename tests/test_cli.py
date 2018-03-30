# -*- coding: utf-8 -*-

"""Tests for the Command Line Interface of the package."""


def test_cli(runner, cli):
    """Test the CLI."""
    result = runner.invoke(cli)
    assert result.exit_code == 0
    assert result.output.startswith('keldcli'), result.output


def test_help_option(runner, cli):
    """Test the --help option."""
    help_result = runner.invoke(cli, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
