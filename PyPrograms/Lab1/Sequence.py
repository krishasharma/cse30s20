#-------------------------------------------------------------------------------------------------------------------------------------------------
#Krisha Sharma 
#krvsharm
#CSE 30-02 Spring 2021
#Lab 1
#Sequence.py 
#----------------------------------------------------------------------------------------------------------------------------------

import math 

def power_remainder(n, m, r): 
    l = 1 
    while True: 
        k = l ** n
        l += 1  
        if k % m == r: 
            yield k 
    
'''
n = user input 
m = divisor
r = remainder of n by m 
Returns a generator of the (infinite) sequence of positive integers that 
are (1) exact powers of n and (2) have remainder r upon division by m.
'''

# end


def common_terms(g, h): #g and h are two different power remainder functions related to each other 
    '''
    Returns a generator of the sequence of terms that are common to the two 
    (increasing) sequences produced by generators g and h.
    '''
    foo = next(g)
    bar = next(h)
    while True: #generator 
            if foo < bar:
                foo = next(g)
            elif foo > bar:
                bar = next(h)
            elif bar == foo: 
                yield foo 
                foo = next(h)   
   # end
# end

def main():
    
    import math 
    
    A = power_remainder(2, 3, 1)
    B = power_remainder(3, 5, 4)
    C = common_terms(power_remainder(2, 3, 1), power_remainder(3, 5, 4))

    print()
    for i in range(15):
      s = "  {0:<12}{1:<12}{2:<12}".format(next(A), next(B), next(C))
      print(s)
    # end
    print()
# end
    

#-------------------------------------------------------------------------------------------------------------------------------
if __name__=='__main__':
    main()

# end
