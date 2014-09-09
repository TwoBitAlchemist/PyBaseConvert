PyBaseConvert
=============

Convert arbitrary numbers between integer bases from 2 to 64.

Installation
------------

    git clone https://github.com/TwoBitAlchemist/PyBaseConvert

Requires Python 2.6+ or Python 3.

Usage
-----

    ./base_convert.py NUM [from_base [to_base [round_to]]]

Convert `NUM`, which is any real number, from `from_base` to `to_base`,
rounding to `round_to` digits in case the result is non-terminating.

If unspecified, both `from_base` and `to_base` are assumed to be 10 and
results are rounded (`round_to`) to 5 places following the radix point.

For convenient use in modules, the convert function can be imported and
used the same way:

    from PyBaseConvert import base_convert

or

    from PyBaseConvert.base_convert import convert

Note that PyBaseConvert should be replaced with whatever directory you
cloned into in case you changed the name.

Once imported, the argument order is the same as given on the command
line. In case the call is malformed, ValueError is raised. On successful
conversions, a string is returned.

Examples
--------

    >>> base_convert.convert(10, 2)
    '2'
    >>> base_convert.convert('a', 16)
    '10'
    >>> base_convert.convert('a', 16, 2)
    '1010'
    >>> base_convert.convert(0.1, from_base=2)
    '.5'
    >>> base_convert.convert(0.1, to_base=2)
    '.00011'
    >>> base_convert.convert(0.1, to_base=2, round_to=9)
    '.000110011'
    >>> base_convert.convert(-8, 10, 5)
    '-13'

Warning About Notation
----------------------

This program uses the following notation for digits in every base (up to the
amount of digits that base needs):

  * `0-9` for the digits 0 through 9.
  * `a-z` for the digits 10 through 35.
  * `A-Z` for the digits 36 through 61.
  * `+` and `/` for the digits 62 and 63.

This may lead to unexpected results for users expecting conformity with
accepted notations for certain commonly used bases. Specifically, this means
that bases like hexadecimal are case sensitive and require lowercase letters
(and that the program will complain that, e.g., `A` is not a valid hex digit).
Likewise, there are several different implementations of base 64 with
varying rules and inconsistencies with one another. If you need more
standard behavior with respect to commonly used bases, please do not use this
program in a production environment.
