import sys as _sys
import traceback as _traceback

from cowpy.cow import Cowacter as _Cowacter


def _cowsay_except(type, value, tracebac):
    class Default(_Cowacter):
        def __init__(self, **kwargs):
            kwargs['body'] = ("     {thoughts}   ^__^\n"
                              "      {thoughts}  ({eyes})\\_______\n"
                              "         (__)\\       )\\/\\\n"
                              "          {tongue}   ||----w |\n"
                              "             ||     ||")
            super().__init__(**kwargs)

    print('Traceback (most recent call last):', file=_sys.stderr)
    _traceback.print_tb(tracebac, file=_sys.stderr)
    print(Default().milk(f'{type.__name__}: {value}'), file=_sys.stderr)


_sys.excepthook = _cowsay_except
