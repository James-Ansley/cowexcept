import traceback as _traceback
from cowpy import cow as _cow
import sys as _sys


def _cowsay_except(type, value, tracebac):
    print('Traceback (most recent call last):', file=_sys.stderr)
    _traceback.print_tb(tracebac, file=_sys.stderr)
    print(_cow.Cowacter().milk(f'{type.__name__}: {value}'), file=_sys.stderr)


_sys.excepthook = _cowsay_except
