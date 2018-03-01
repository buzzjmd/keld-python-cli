# -*- coding: utf-8 -*-

"""Test fixtures."""

import keldcli
import pytest
from click.testing import CliRunner


@pytest.fixture(scope='function')
def runner():
    """Create the Click test runner."""
    runner = CliRunner()
    return runner


@pytest.fixture(scope='module')
def cli():
    """Pass the command line interface as a fixture."""
    return keldcli.cli
