import sys as _sys
from contextlib import redirect_stderr as _redirect_stderr
from io import StringIO as _StringIO
from typing import TextIO as _TextIO

import cowsay as _cowsay

_cow = _cowsay.get_cow("default")


def _cowsay_except(type, value, tracebac):
    error = _StringIO()
    with _redirect_stderr(error):
        _sys.__excepthook__(type, value, tracebac)
    cow = _cowsay.cowsay(error.getvalue(), cowfile=_cow, wrap_text=False)
    print(cow, file=_sys.stderr)


def activate():
    _sys.excepthook = _cowsay_except


def deactivate():
    _sys.excepthook = _sys.__excepthook__


def set_cow(cow_name: str):
    """
    :param cow_name: The name of a cowfile defined in the python-cowsay package

    :raises ValueError: If the cowfile cannot be found.
    """
    if cow_name not in _cowsay.list_cows():
        raise ValueError(f"Unrecognised Cow File: '{cow_name}'")
    global _cow
    _cow = _cowsay.get_cow(cow_name)


def set_cow_from_file(f: _TextIO, escapes=None):
    """
    :param f: A text stream of a cowfile
    :param escapes: custom escape codes for the file if needed
    """
    global _cow
    _cow = _cowsay.read_dot_cow(f, escapes=escapes)
