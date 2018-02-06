# -*- coding: utf-8 -*-

import keldcli


def test_keldcli():
    assert keldcli.cli() is None


def test_keldcli_as_module():
    import subprocess
    returncode = subprocess.call(['python', '-m', 'keldcli'])
    assert(returncode == 0)


def test_keldcli_as_script():
    import subprocess
    returncode = subprocess.call(['keld'])
    assert(returncode == 0)
