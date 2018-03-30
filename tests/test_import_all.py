# -*- coding: utf-8 -*-

# flake8: noqa

import keldcli
from keldcli import *


def test_import_all():
    """Test what has been included in the __all__ variable of __init__.py"""
    assert cli
    assert keldcli.cli is cli
    assert __distribution__
    assert keldcli.__distribution__ is __distribution__
    assert __title__
    assert keldcli.__title__ is __title__
    assert __title__ == "keldcli"
    assert __version__
    assert keldcli.__version__ is __version__
