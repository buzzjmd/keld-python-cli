# -*- coding: utf-8 -*-

import pytest

import keldcli


def test_keldcli():
    with pytest.raises(SystemExit) as excinfo:
        keldcli.cli()
    system_exit = excinfo.value
    assert system_exit.code == 0


def test_keldcli_as_module():
    import subprocess
    returncode = subprocess.call(['python', '-m', 'keldcli'])
    assert(returncode == 0)


def test_keldcli_as_script():
    import subprocess
    returncode = subprocess.call(['keld'])
    assert(returncode == 0)
