#SubsetTest3.py

# Python program to print all 
# sublist from a given list 
# function to generate all the sub lists

import sys
import math 
import itertools

n = int(sys.argv[1])
k = int(sys.argv[2])

def subsets(n, k):
    if n < k or k < 0:
        return []
    if k == n:
        return [list(range(k))]
    return subsets(n-1, k) + [s+[n-1] for s in subsets(n-1, k-1)]
    print(subsets(n, k))

def main():
    subsets(n , k) 

if __name__=='__main__':
    main()