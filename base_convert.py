#! /usr/bin/env python
"""
Convert arbitrary numbers between integer bases from 2 to 64.
"""
import string
import sys
from decimal import Decimal


ALL_DIGITS = ''.join(map(str, range(10))) + string.ascii_letters + '+/'
DIGIT_MAP = {k:v for k,v in enumerate(ALL_DIGITS)}
DIGIT_RMAP = {v:k for k,v in enumerate(ALL_DIGITS)}


def handle_error(e):
    pass


def digit_error(digit, base):
    """
    Report an invalid digit in the given base.
    """
    message = '%s is not a valid digit in base %s.' % (digit, base)
    handle_error(message)
    raise ValueError(message)


def convert(number, from_base=10, to_base=10, round_to=5):
    """
    Convert number between specified bases, rounding to round_to digits.
    """
    try:
        from_base, to_base, round_to = map(int, (from_base, to_base, round_to))
    except ValueError as v:
        offender = v.args[0].split(':')[1].lstrip()
        handle_error('Base and rounding arguments must be integers, '
                     'not %s.' % offender)
        raise
    for base in (from_base, to_base):
        if not 1 < base <= len(ALL_DIGITS):
            message = 'Unsupported base: %s' % base
            handle_error(message)
            raise ValueError(message)
    try:
        int_part, frac_part = str(number).split('.')
    except ValueError:
        int_part = str(number)
        frac_part = ''
    finally:
        if int_part:
            try:
                int_part = int(int_part, from_base)
            except ValueError:
                integer = 0
                for i, d in enumerate(reversed(int_part)):
                    d_value = DIGIT_RMAP[d]
                    if d_value >= from_base:
                        digit_error(d, from_base)
                    integer += d_value * from_base ** i
                int_part = integer
        else:
            int_part = 0

    int_digits = []
    quotient = abs(int_part)
    while quotient > 0:
        int_digits.append(quotient % to_base)
        quotient = int(quotient / to_base)

    result = '' if int_part == abs(int_part) else '-'
    result += ''.join((DIGIT_MAP[k] for k in reversed(int_digits)))
    fraction = 0
    for i, d in enumerate(frac_part):
        d_value = DIGIT_RMAP[d]
        if d_value >= from_base:
            digit_error(d, from_base)
        fraction += d_value * from_base ** -(i+1)
    frac_digits = []
    product = fraction
    while product > 0 and len(frac_digits) < round_to:
        product *= to_base
        frac_digits.append(int(product))
        product -= int(product)
    if frac_digits:
        result += '.' + ''.join(map(str, frac_digits))
    return result if result else '0'


if __name__ == '__main__':
    handle_error = sys.exit
    try:
        sys.argv[1]
    except IndexError:
        print('Usage: %s NUM [from_base [to_base [round_to]]]' % sys.argv[0])
        sys.exit(1)
    print(convert(*sys.argv[1:]))
