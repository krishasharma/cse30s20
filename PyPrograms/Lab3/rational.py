#------------------------------------------------------------------------------
# Krisha Sharma 
# krvsharm
# CSE 30-02 Spring 2021
# PA 4
# rational.py 
# Represents raitonal numbers. 
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
from rational import *
from decimal import *

def _gcd(a, b): 
    while a % b != 0:
        olda = a
        oldb = b
        a = oldb
        b = olda % oldb
    return b

class Rational(object):
    def __init__(self, n, d=1):
        #Initialize a Rational object.
        factor = _gcd(n, d)
        self.numer = n // factor
        self.denom = d // factor

    def __add__(self, other):
        #Return the sum of two rational numbers.
        return Rational((self.numer * other.denom)+(other.numer * self.denom), (self.denom * other.denom))

    def __eq__(self, other):
        #Return True if self == other, False otherwise.
        fac1 = other.denom
        fac2 = self.denom
        
        self.numer = self.numer * fac1
        self.denom = self.denom * fac1
        
        other.numer = other.numer * fac2
        other.denom = other.denom * fac2
        
        return self.numer == other.numer

    def __float__(self):
        #Return the float equivalent of self.
        return float(self.numer/self.denom)

    def __ge__(self, other):
        #Return true if self >= other, False otherwise.
        fac1 = other.denom
        fac2 = self.denom
        
        self.numer = self.numer * fac1
        self.denom = self.denom * fac1
        
        other.numer = other.numer * fac2
        other.denom = other.denom * fac2
        
        return self.numer >= other.numer

    def __gt__(self, other):
        #Return true if self > other, False otherwise.
        fac1 = other.denom
        fac2 = self.denom
        
        self.numer = self.numer * fac1
        self.denom = self.denom * fac1
        
        other.numer = other.numer * fac2
        other.denom = other.denom * fac2
        
        return self.numer > other.numer

    def __le__(self, other):
        #Return true if self <= other, False otherwise.
        fac1 = other.denom
        fac2 = self.denom
        
        self.numer = self.numer * fac1
        self.denom = self.denom * fac1
        
        other.numer = other.numer * fac2
        other.denom = other.denom * fac2
        
        return self.numer <= other.numer

    def __lt__(self, other):
        #Return true if self < other, False otherwise.
        fac1 = other.denom
        fac2 = self.denom
        
        self.numer = self.numer * fac1
        self.denom = self.denom * fac1
        
        other.numer = other.numer * fac2
        other.denom = other.denom * fac2
        
        return self.numer < other.numer

    def __mul__(self, other):
        #Return the product of two rational numbers.
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __ne__(self, other):
        #Return False if self == other, True otherwise.
        if self.numer == other.numer and self.denom == other.denom:
            return False 
        else: 
            return True 

    def __repr__(self):
        #Return the detailed string representation of a rational number.
        return 'rational.Rational({}, {})'.format(self.numer, self.denom)

    def __str__(self):
        #Return the string representation of a rational number.
        if (self.denom == 1):
            return str(self.numer) + "/" + str(self.denom)
        else:
            return str(self.numer) + "/" + str(self.denom)

    def __sub__(self, other):
        #Return the difference of two rational numbers.
        fac1 = other.denom
        fac2 = self.denom
        return Rational(self.numer * fac1 - other.numer * fac2, self.denom * other.denom)

    def __truediv__(self, other):
        #Return the quotient of two rational numbers.
        return self * other.inverse()

    def inverse(self):
        #Return the multiplicative inverse of a rational number.
        return Rational(self.denom, self.numer)

#------------------------------------------------------------------------------
#driver code
#------------------------------------------------------------------------------
#def main():

# end

#------------------------------------------------------------------------------
#if __name__=='__main__':
   #main()




