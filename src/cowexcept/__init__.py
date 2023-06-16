import sys
from contextlib import redirect_stderr
from io import StringIO
from typing import TextIO

import cowsay

__all__ = ["activate", "deactivate", "set_cow", "set_cow_from_file"]

_cow = cowsay.get_cow("default")

EXCEPT_HOOK = sys.excepthook


def _cowsay_except(type, value, tracebac):
    error = StringIO()
    with redirect_stderr(error):
        EXCEPT_HOOK(type, value, tracebac)
    cow = cowsay.cowsay(error.getvalue(), cowfile=_cow, wrap_text=False)
    print(cow, file=sys.stderr)


def activate():
    global EXCEPT_HOOK
    EXCEPT_HOOK = sys.excepthook
    sys.excepthook = _cowsay_except


def deactivate():
    sys.excepthook = sys.__excepthook__


def set_cow(cow_name: str):
    """
    :param cow_name: The name of a cowfile defined in the python-cowsay package

    :raises ValueError: If the cowfile cannot be found.
    """
    if cow_name not in cowsay.list_cows():
        raise ValueError(f"Unrecognised Cow File: '{cow_name}'")
    global _cow
    _cow = cowsay.get_cow(cow_name)


def set_cow_from_file(f: TextIO, escapes=None):
    """
    :param f: A text stream of a cowfile
    :param escapes: custom escape codes for the file if needed
    """
    global _cow
    _cow = cowsay.read_dot_cow(f, escapes=escapes)
