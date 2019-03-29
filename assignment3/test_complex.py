#!/usr/bin/python
import cmath
from complex import Complex

# Test functions
def test_add():
    """Test for a complex number added with a complex number"""
    assert (Complex(2, 3) + Complex(1, 4)) == (3+7j)

def test_sub():
    """Test for a complex number subtracted with a complex number"""
    assert (Complex(2, 3) - Complex(1, 4)) == (1-1j)

def test_conjugate():
    """Test for a complex number that is conjugated"""
    assert (Complex(2, 3).conjugate()) == (2-3j)

def test_modulus():
    """Test for the modulus of a complex number"""
    assert (Complex(3, 4)).modulus() == 5.0

def test_eq():
    """Tests the equality between two complex numbers"""
    assert (Complex(2, 3) == Complex(2, 3))

def test_custom_to_python():
    """
    Tests operation between our Complex class and Python's
    build-in complex.
    Both are complex numbers.
    """
    assert (Complex(2, 3) + (2+2j)) == Complex(4, 5)

def test_radd():
    """
    Tests addition starting with a Python built-in operation
    combined with an operation from our custom Complex class
    Both are complex numbers.
    """
    assert ((2+2j) + (Complex(2, 3))) == Complex(4, 5)

def test_rmul():
    """
    Tests multiplication starting with a Python built-in operation
    combined with an operation from our custom Complex class.
    Both are complex numbers.
    """
    assert ((2+3j) * (Complex(1, 2))) == Complex(2, 6)

def test_rsub():
    """
    Tests subtraction starting with a Python built-in operation
    combined with an operation from our custom Complex class.
    Both are complex numbers.
    """
    assert ((2+3j) - (Complex(1, 2))) == Complex(1, 1)

def test_real_with_imag():
    """
    This serves to test rmul when the first number is not a
    complex number.
    """
    assert (4*(Complex(3, 4)) - 2) == Complex(10, 16)

def test_rsub_real():
    """Tests rsub when the first number is not a complex number."""
    assert (5-(Complex(3, 4))) == Complex(2, -4)

def test_radd_real():
    """Tests radd when the first number is not a complex number."""
    assert (5+(Complex(3, 4))) == Complex(8, 4)

# 3.2
test_add()
test_sub()
test_conjugate()
test_modulus()
test_eq()

# 3.4
test_custom_to_python()
test_radd()
test_rmul()
test_rsub()
test_real_with_imag()

# extra tests
test_rsub_real()
test_radd_real()
