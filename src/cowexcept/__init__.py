# Copyright 2025 cowexcept contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import sys
from contextlib import redirect_stderr
from io import StringIO
from typing import TextIO

import cowsay

__all__ = ["activate", "deactivate", "set_cow", "set_cow_from_file"]

_cow = cowsay.get_cow("default")


def _cowsay_except(type, value, tracebac):
    error = StringIO()
    with redirect_stderr(error):
        sys.__excepthook__(type, value, tracebac)
    cow = cowsay.cowsay(error.getvalue(), cowfile=_cow, wrap_text=False)
    print(cow, file=sys.stderr)


def activate():
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
