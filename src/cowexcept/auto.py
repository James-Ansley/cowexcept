import sys as _sys
from . import _cowsay_except

_sys.excepthook = _cowsay_except
