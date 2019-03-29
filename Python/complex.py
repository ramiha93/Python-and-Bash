#!/usr/bin/python
import math

class Complex:


    def __init__(self, real, imag):
        """
        Parameters
        ----------
        real : int
            The real portion of the complex number
        imag : int
            The imaginary portion of the complex number
        """

        self.real = real
        self.imag = imag


    # Assignment 3.3

    def conjugate(self):
        """(self.real+(-self.imag))"""
        return (Complex((self.real), (-(self.imag))))

    def modulus(self):
        """sqrt(real²+imag²)"""
        modulus_result = math.sqrt(((self.real)**2) + ((self.imag)**2))
        return modulus_result

    def __add__(self, other):
        """addition"""
        self.real+=other.real
        self.imag+=other.imag
        return (Complex(self.real, self.imag))

    def __sub__(self, other):
        """subtraction"""
        self.real-=other.real
        self.imag-=other.imag
        return (Complex(self.real, self.imag))

    def __mul__(self, other):
        """multiplication"""
        self.real*=other.real
        self.imag*=other.imag
        return (Complex(self.real, self.imag))

    def __eq__(self, other):
        """checking if two numbers are equal"""
        return (self.real+(self.imag*1j)) == (other.real+(other.imag*1j))
        #return (Complex(self.real, self.imag) == Complex(other.real, other.imag))

    # Assignment 3.4
    def __radd__(self, other):
        """radd"""
        #Verifies if self is not a complex number
        if not isinstance(other, complex):
            #Transform real number into a seemingly complex number
            c = Complex(other.real, 0)
            #Proceed with the addition
            radd_res_real1 = (c.real)+(self.real)
            radd_res_imag1 = (c.imag)+(self.imag)
            return (Complex(radd_res_real1, radd_res_imag1))
        else:
            #Both numbers are already in the form of complex numbers
            radd_res_real2 = (other.real)+(self.real)
            radd_res_imag2 = (other.imag)+(self.imag)
            return (Complex(radd_res_real2, radd_res_imag2))

    def __rsub__(self, other):
        """rsub"""
        #Verifies if self is not a complex number
        if not isinstance(other, complex):
            #Transform real number into a seemingly complex number
            c = Complex(other.real, 0)
            #Proceed with the subtraction
            rsub_res_real1 = (c.real)-(self.real)
            rsub_res_imag1 = (c.imag)-(self.imag)
            return (Complex(rsub_res_real1, rsub_res_imag1))
        else:
            #Both numbers are already in the form of complex numbers
            rsub_res_real2 = (other.real)-(self.real)
            rsub_res_imag2 = (other.imag)-(self.imag)
            return (Complex(rsub_res_real2, rsub_res_imag2))

    def __rmul__(self, other):
        """rmul"""
        #Verifies if self is not a complex number
        if not isinstance(other, complex):
            #Transform real number into a seemingly complex number
            c = Complex(other.real, 0)
            #Proceed with the multiplication
            rmul_res_real1 = (c.real)*(self.real)
            rmul_res_imag1 = (c.real)*(self.imag)
            return (Complex(rmul_res_real1, rmul_res_imag1))
        else:
            #Both numbers are already in the form of complex nunbers
            rmul_res_real2 = (self.real)*(other.real)
            rmul_res_imag2 = (self.imag)*(other.imag)
            return (Complex(rmul_res_real2, rmul_res_imag2))


    # Optional, possibly useful methods

    # Allows you to write `-a`
    def __neg__(self):
        pass

    # Make the `complex` function turn this into Python's version of a complex number
    def __complex__(self):
        pass
