#SubsetsTest.py 
import sys 
import math 
#---------------------------------------------------------------------------------------------------------
'''
import itertools
#def findsubsets(s, n):
def findsubsets(n, k):
    return [set(i) for i in itertools.combinations(n, k)]
      
#driver Code
n = {1, 2, 3, 4}
k = 3

def main():
    print(findsubsets(n, k))

if __name__=='__main__':
    main() 
'''
#---------------------------------------------------------------------------------------------------------
'''
# Function to create combinations without itertools
def findsubsets(n, k):
    if k == 0:
        return [[]]
      
    B =[]
    for i in range(0, len(n)):
        m = n[i]
        remn = n[i + 1:]
        for p in findsubsets(remn, k-1):
            B.append([m]+p)
              
    return B
  
# Driver code
n = {1, 2, 3, 4}
k = 3

if __name__=="__main__":
    print(findsubsets(n, k)) #print(findsusbets([x for x in arr], 2))
'''
#---------------------------------------------------------------------------------------------------------
'''
def sub(l):
    if l == []:
        return [[]]

    x = sub(l[1:])

    return x + [[l[0]] + y for y in x]
'''
#---------------------------------------------------------------------------------------------------------
'''
def decimalToBinary(n): #converting decimal to binary
    b = 0
    i = 1
    while (n != 0):
        r = n % 2
        b+= r * i
        n//= 2
        i = i * 10
    return b
def makeList(k): #list of the binary element produced
    a =[]
    if(k == 0):
        a.append(0)
    while (k>0):
        a.append(k % 10)
        k//= 10
    a.reverse()
    return a
def checkBinary(bin, l):
    temp =[]
    for i in range(len(bin)):
        if(bin[i]== 1):
            temp.append(l[i])
    return temp

l =[1, 2, 3, 4]
binlist =[]
subsets =[]
n = len(l)

for i in range(2**n):
    s = decimalToBinary(i)
    arr = makeList(s)
  
    binlist.append(arr)
    
    for i in binlist:
        k = 0
        while(len(i)!= n):
            i.insert(k, 0) #representing the binary equivalent according to len(l)
            k = k + 1
for i in binlist:
    subsets.append(checkBinary(i, l)) #print(binlist) print this for more understanding

print(subsets)
'''
#---------------------------------------------------------------------------------------------------------

# Python3 program to print all subset combination of n elements in an n element given set of r (k) element.
 
# arr[] ---> Input Array
# data[] ---> Temporary array to store current combination
# start & end ---> Staring and Ending indexes in arr[]
# index ---> Current index in data[]
# r ---> Size of a combination to be printed

def combinationUtil(arr, n, k, index, data, i): #Current combination is ready to be printed, print it
    if(index == k):
        for j in range(k):
            print(data[j], end = " ")
        print(" ")
        return
 
    #when no more elements are there to put in data[]
    if(i >= n):
        return
 
    #current is included, put next at next location
    data[index] = arr[i]
    combinationUtil(arr, n, k, index + 1, data, i + 1)
     
    #current is excluded, replace it with next (Note that i+1 is passed, but index is not changed)  
    combinationUtil(arr, n, k, index, data, i + 1)
 
 
#the main function that prints all combinations of size k in arr[] of size n. This function mainly uses combinationUtil()
def printcombination(arr, n, k):
 
    #a temporary array to store all combination one by one
    data = list(range(k))
     
    #print all combination using temporary array 'data[]'
    combinationUtil(arr, n, k, 0, data, 0)
 
#driver code
arr = [10, 20, 30, 40, 50]
#arr = [1, 2, 3]
k = 3
n = len(arr)

printcombination(arr, n, k)