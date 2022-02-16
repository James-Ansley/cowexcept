import sys as _sys
from io import StringIO as _StringIO

from cowsay import cowsay as _cowsay


def _cowsay_except(type, value, tracebac):
    _sys.stderr = error = _StringIO()
    _sys.__excepthook__(type, value, tracebac)
    _sys.stderr = _sys.__stderr__
    cow = _cowsay(
        error.getvalue(),
        wrap_text=False,
    )
    print(cow, file=_sys.stderr)


_sys.excepthook = _cowsay_except
