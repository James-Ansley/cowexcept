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

## Should you install this?

Probably not!
This is a hastily hacked together project that does not do anything useful. But!
It might still spice up those error messages and make them a bit less draining
to read.

## Usage

All you have to do to get started is `import cowexcept` and then any exceptions
whenceforth will be in beautiful cowsay format:

    >>> import cowexcept
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
