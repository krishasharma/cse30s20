# SubsetExtra.py 

import math 
import sys 
import itertools

'''
section notes 
what to_string will do 
{1, 2, 3}
B = ["*", 1, 1, 1] = 1, 2, 3
{1, 3}
["*", 1, 0]

1, 2
1, 3
2, 3 

[1, 0, 1] = 1, 3
[1, 1, 0] = 1, 2
[0, 1, 1] = 2, 3 
using recusrion 

to string is trying to print a list B 
print subset prints the power set to a certain length k 


n = len(B) - 1 (in printSubsets)
'''

n = int(sys.argv[1])
k = int(sys.argv[2])


print("n and k:", sys.argv[1], sys.argv[2])


my_set = {1}
s = 1
for i in range(n):
    my_set.add(s)
    s = s + 1 
my_set = set(my_set)
print("set is = ", my_set)
B = list(my_set) #S 

'''
B = list(range(0, n+1))
B = [0] * n 
i = 1 
'''

'''
def to_string(B):
    B = list(range(0, n+1))
    B = [0] * n 
    B.insert(0, '*')
    for B[i] = 0:
        B.insert(0, '*')
        pass  
        if B[i] = 0:
            print 


    for i in range(B):
        B.append(B[i])
    B[i] = [i + 1]
    print("k=", k, "is", B[i])
    print("the bit list:", B)
    B[:i] = ['*', 1]
    print("list changed: ", B)

    print(B)
    for B[:i] where B = 1: 
'''
'''
def subset(B, n, k, i):
    if i < n: #end for recursion, pass through all elements 
        if k == 0: 
            print(' ')
        else: 
            print(B[i])
            subset(B, n, k-1, i+1) #uses the number IN the current index
            subset(B, n, k, i+1) #doesn't use the number in the current index 

subset(B, n, k, i)
'''

#def inclued(n , k):

#def exclude(n, k):

'''
def printSubsets(B, k, i):
    #n = len(B) - 1
    N = int(pow(2, len(B))) #N stores the total number of subsets
    s = set()
    #S.sort() #sort the set 
    for i in range(N): #generate each subset one by one
        subset = []
        #B = []
        #for k in range(len(S)):
        for j in range(len(B)): #check every bit of 'i'
            #if i & (1 << k):
            if i & (1 << j): #if j'th bit of 'i' is set, append 'S[j]' to the subset
                #subset.append(S[k])
                subset.append(B[j])
                #B.append(S[j])
        s.add(str(subset)) #insert the subset into the set
        #s.add(str(B))
    for subset in s: #print all subsets present in the set
        print(subset)
    #for B in s: 
    #    print(B)
'''

def to_string(B): #bit list converts to subset
    setString = '{' #+=
    button = 0 
    for i in range(len(B)): #i is index of bit list
        if B[i] == 1: 
            if(button == 1):
                setString += ", " #+= appending for strings 
            setString += str(i) #+= because adding to whats in set string
            button = 1
    setString += "}"
    return setString

def printSubsets(B, k, i):
    if k == 0: #call to_string
        print(B)
        print(to_string(B))
    elif k > n - i + 1:
        return #pass
    else:
        B[i] = 1
        printSubsets(B, k-1, i+1) 
        B[i] = 0 
        printSubsets(B, k, i+1)


def main():
    #B = list(range(0, n+1))
    B = [0] * (n + 1) 
    B[0] = '*'
    #print(B)
    i = B[1]
    #to_string(B)
    printSubsets(B, k, 1)
    #gen_subsets(n, k)
    #subset(n, k)

if __name__ == '__main__':
   main()
    


#def powerset(iterable):
    #from itertools import combinations
    #n = list(iterable)
    #return [combinations(n, k) for k in range(len(n)+1)]


'''
def subset(n, k):
    if k == 0:
        return 1
    if n == k:
        return 1
    else:
        return subset(n-1, k-1) + subset(n-1, k)
'''



'''
def printSubsets(B, k, i):
    n = len(B) - 1 
    printSubsets(B, k , i+1) #inclusive
    B[i] = 1

    printSubsets(B, k-1, i+1) #exclusive 
    B[i] = 0 
'''

'''
def printSubsets(B, k, i):
    #B = list(range(0, n+1))
    B = [0] * n 
    n = len(B) - 1
    if n < k: 
        return 0 
    if n == 0: 
        return 1 
    result = to_string(n-1, k) + to_string(n//2, k -1)
    print(result)
 '''   
