#------------------------------------------------------------------------------
# Krisha Sharma 
# krvsharm
# CSE 30-02 Spring 2021
# Lab 3
# MoreContinuedFractions.py 
# Program that represents raitonal numbers, the rational approximation to pi, 
# as well as the equivalent Decimal object, correct to 100 places and the 
# ordinary conntinued fraction. 
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
from rational import *
from decimal import *
import sys
import math

def CF2R(L): 
    numer = int(L[-1])
    denom = 1
    finalresult = Rational(numer, 1) # initilize to zero
    L.pop(-1)
    for k in L[-1::-1]: 
        numer = int(L[-1])
        current = Rational(numer, 1)
        finalresult = current + finalresult.inverse() # calling Rational class inverse
        L.pop(-1)
    return finalresult 

def R2CF(x):
    # inverse of CF2R(L)
    # takes a Rational object as input, and returning a list representing 
    # the continued fraction for that rational number as output
    # uses _gcd from rational class to make function recursive 
    L = []
    a = x.numer
    b = x.denom  
    while a % b != 0:
        m = a // b #7
        rem = a % b 
        a = b 
        b = rem 
        L.append(m)
    m = a // b #7
    L.append(m)
    return L 


# Check that both of the expressions CF2R(R2CF(x))==x and R2CF(CF2R(L))==L 
# return True for any Rational object x and any list L. 

def GCF2R(L):
    # takes a list L (of odd length) representing a generalized continued fraction, and 
    # returns the corresponding rational number as an object of type Rational

    # if GCF2R() is called on an even length list? A simple way to avoid raising an exception is 
    # by adding a base case for lists of length 0, which just returns Rational(1). 
    # This effectively appends 1 to the list, making it even length.
    if len(L) >= 2:  
        return Rational(L[0]) + (Rational(L[1]) / GCF2R(L[2::]))
    if len(L) == 1:
        return Rational(L[0])
    if len(L) == 0: 
        return Rational(1)

def  pi_gen():
    # returning a generator object that produces the sequence 
    # [0, 4, 1, 12, 3, 22, 5, 32, 7, 42 … … ] = [0, 4] + [2𝑘𝑘 − 1, 𝑘𝑘2]𝑘𝑘=1 ∞.
    yield 0
    yield 4
    k = 1 
    while True:
        yield(2*k-1)
        yield(k**2)
        k += 1

def main():
    getcontext().prec = 101
    i = Rational(1137,158)
    L = []
    generator = pi_gen()
    for x in range(265):
        L.append(next(generator)) 
    a = (GCF2R(L))
    print() # a blank line 
    print(str(a)) # your rational approximation to pi
    print() # a blank line
    piDec = (Decimal(a.numer) / Decimal(a.denom))   
    print(piDec) # the equivalent Decimal object, correct to 100 places
    print() # a blank line 
    var = R2CF(a)
    print(var) # the equivalent ordinary continued fraction
    print() # a blank line 

if __name__=='__main__': 
   main()