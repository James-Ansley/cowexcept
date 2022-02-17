# CowExcept

Spice up those exceptions with cowexcept!

     ______________________________________ 
    < NameError: name 'baz' is not defined >
     -------------------------------------- 
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\
                 ||----w |
                 ||     ||

## Install

    pip install cowexcept

## Usage

All you have to do to get started is activate `cowexcept` and then any
exceptions whenceforth will be in beautiful cowsay format:

    >>> import cowexcept
    >>> cowexcept.activate()
    >>> 1/0
     _______________________________________ 
    / Traceback (most recent call last):    \
    |   File "...", line 1, in ...          |
    \ ZeroDivisionError: division by zero   /
     --------------------------------------- 
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||

The `cowexcept.activate()` call is to avoid unused import flags from IDEs or
style checkers and avoiding any import-time side effects. If unused imports and
import-time side effects do not bother you, and you would prefer to avoid the
horrible extra line used to explicitly activate `cowexcept`,
use `import cowexcept.auto` instead and this will activate `cowexcept` on
import.

To deactivate `cowexcept` call `cowexcept.deactivate()` and any exceptions will
be handled as before.
