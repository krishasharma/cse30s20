#Quiz2Question2.py 

import math 

def sequence_gen(a, b):
    #begin solution
    l = 1 
    while True:
        r = 1 
        k = l ** a
        l += 1  
        if k % b == r: 
            yield k 
    #end solution

print(sequence_gen(3, 5))


'''
n = user input 
m = divisor
r = remainder of n by m 
Returns a generator of the (infinite) sequence of positive integers that 
are (1) exact powers of n and (2) have remainder r upon division by m.
'''

