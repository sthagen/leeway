import sys

import leeway.__main__
from leeway.cli import main


def test_main():
    assert main([]) == 0


def test_main_sys():
    assert main(sys.argv) == 0


def test_main_none():
    assert main(None) == 0


def test_main_some():
    assert main([1, 2, False, None, 'foo']) == 0


def test_main_folder():
    assert leeway.__main__.main(None) == 0
