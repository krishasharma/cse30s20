#NChooseK.py
import math 

#n = int(input("n = "))
#k = int(input("k = "))



#------------------------------------------------------------------------
n = 5 
k = 3 

def factorial(n):
    prod = 1
    for k in range (2, n+1): 
        prod = prod * k 
    return prod 

def recfactorial(n):
    if n == 0:
        return 1
    return n * recfactorial(n-1)

def main():
    for n in range (0, 11):
        print(factorial(n), recfactorical(n))

if __name__=='__main__':
    main() 
   