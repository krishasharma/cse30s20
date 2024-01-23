#RecursionBinomialCoefficient.py

import sys
import math 
sys.setrecursionlimit(2000)

n=int(input("Enter n:"))
k=int(input("Enter k:"))

def fac(b):
    if b==1:
        return 1
    else:
        return b * fac(b-1)

def combinations(n,k):
    result = (fac(n)) / (fac(k) * fac(n-k))
    return result


print(n, k, combinations(n,k))

