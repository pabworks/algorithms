"""Implementation of recursive integer multiplication algorithm
"""
# pylint: disable=no-self-use,invalid-name
import unittest

def int_mul(x, y):
    """Multiplies two integers with the same number of digits
    using the recursive multiplication algorithm
    Works for integers with n_digits being some power of 2
    """
    x, y = str(x), str(y)
    assert len(x) == len(y), "x and y must be integers of the same length"
    n = len(x)
    # base case
    if n == 1:
        return int(x) * int(y)
    a, b = int(x[:len(x) // 2]), int(x[len(x) // 2:])
    c, d = int(y[:len(y) // 2]), int(y[len(y) // 2:])
    ac = int_mul(a, c)
    bd = int_mul(b, d)
    ad = int_mul(a, d)
    bc = int_mul(b, c)
    return 10 ** n * ac + 10 ** (n // 2) * (ad + bc) + bd


class TestIntMul(unittest.TestCase):
    """Test cases for integer multiplication
    """

    def test(self):
        """Test some basic integer multiples
        """
        assert int_mul(2, 3) == 6
        assert int_mul(12, 12) == 144
        assert int_mul(1234, 5678) == 7006652
