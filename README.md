PyBaseConvert
=============

Convert arbitrary numbers between integer bases from 2 to 64.

Installation
------------

    git clone https://github.com/TwoBitAlchemist/PyBaseConvert

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
