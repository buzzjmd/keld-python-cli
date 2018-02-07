# -*- coding: utf-8 -*-

# flake8: noqa

import keldcli

from keldcli import *


def test_import_all():
    """Test what has been included in the __all__ variable of __init__.py"""
    assert(keldcli.cli is cli)
