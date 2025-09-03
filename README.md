# CowExcept

[![Repository](https://img.shields.io/badge/jamesansley%2Fcowexcept-102335?logo=codeberg&labelColor=07121A)](https://codeberg.org/jamesansley/cowexcept)
[![PyPi](https://img.shields.io/pypi/v/cowexcept?label=PyPi&labelColor=%23ffd343&color=%230073b7)](https://pypi.org/project/cowexcept/)
[![License](https://img.shields.io/badge/Apache--2.0-002d00?label=license)](https://codeberg.org/jamesansley/cowexcept/src/branch/main/LICENSE)

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
     _____________________________________ 
    / Traceback (most recent call last):  \
    |   File "...", line 1, in ...        |
    |     1 / 0                           |
    \ ZeroDivisionError: division by zero /
     ------------------------------------- 
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

### Using Your Own Cows

You can specify alternative cows to display using the `set_cow`
and `set_cow_from_file` functions.

The `set_cow` function takes the name of any cowfile included in
the [python-cowsay](https://github.com/James-Ansley/cowsay) package and sets the
cow to be displayed in exceptions.

    >>> import cowexcept
    >>> cowexcept.activate()
    >>> cowexcept.set_cow("dragon-and-cow")
    >>> 1 / 0
     _____________________________________ 
    / Traceback (most recent call last):  \
    |   File "...", line 1, in ...        |
    |     1 / 0                           |
    \ ZeroDivisionError: division by zero /
     -------------------------------------
                           \                    ^    /^
                            \                  / \  // \
                             \   |\___/|      /   \//  .\
                              \  /O  O  \__  /    //  | \ \           *----*
                                /     /  \/_/    //   |  \  \          \   |
                                @___@`    \/_   //    |   \   \         \/\ \
                               0/0/|       \/_ //     |    \    \         \  \
                           0/0/0/0/|        \///      |     \     \       |  |
                        0/0/0/0/0/_|_ /   (  //       |      \     _\     |  /
                     0/0/0/0/0/0/`/,_ _ _/  ) ; -.    |    _ _\.-~       /   /
                                 ,-}        _      *-.|.-~-.           .~    ~
                \     \__/        `/\      /                 ~-. _ .-~      /
                 \____(oo)           *.   }            {                   /
                 (    (--)          .----~-.\        \-`                 .~
                 //__\\  \__ Ack!   ///.----..<        \             _ -~
                //    \\               ///-._ _ _ _ _ _ _{^ - - - - ~


You can also specify custom cows by passing in a cowfile or TextIO stream to
the `set_cow_from_file` function:

    >>> from io import StringIO
    >>> import cowexcept
    >>> cowexcept.set_cow_from_file(StringIO("""
    ... $the_cow = <<EOC;
    ...          $thoughts
    ...           $thoughts
    ...            ___
    ...           (o o)
    ...          (  V  )
    ...         /--m-m-
    ... EOC
    ... """))
    >>> cowexcept.activate()
    >>> 1 / 0
     _____________________________________ 
    / Traceback (most recent call last):  \
    |   File "...", line 1, in ...        |
    |     1 / 0                           |
    \ ZeroDivisionError: division by zero /
     -------------------------------------
             \
              \
               ___
              (o o)
             (  V  )
            /--m-m-
