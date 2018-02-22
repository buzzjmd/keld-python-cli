# -*- coding: utf-8 -*-

"""Python specific tests."""


def test_pythons():
    """Test Pythons.

    Use this test to check coverage,
    i.e. make sure both python2 and python3 have been tested.
    """
    import sys
    if sys.version_info.major < 3:
        # Python 2 or earlier
        assert sys.version_info.major < 3
    else:
        # Python 3 or later
        assert sys.version_info.major >= 3
