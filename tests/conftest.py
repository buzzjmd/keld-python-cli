# -*- coding: utf-8 -*-

"""Test fixtures."""

from click.testing import CliRunner

import pytest


@pytest.fixture(scope='function')
def runner():
    """Create the Click test runner."""
    runner = CliRunner()
    return runner
