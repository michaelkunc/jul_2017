import random
from string import ascii_uppercase, digits


def order_number():
    """Return fake order number in the following format 714-EO1-56237-B"""
    prefix = ''.join(random.sample(digits, 3))
    mid = ''.join(random.sample(ascii_uppercase, 2) + random.sample(digits, 1))
    end = ''.join(random.sample(digits, 5))
    post = ''.join(random.sample(ascii_uppercase, 1))
    return '{0}-{1}-{2}-{3}'.format(prefix, mid, end, post)
