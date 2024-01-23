# SubsetTest5.py 

import math 
import sys 
import itertools
'''
set = list(range(n))

def to_string(B): #converts bit list into subset 
#take n  
#make it into a set of numbers in accending order starting at 1 
#creates the numeric n-element set from user input 

#end 
'''
'''
section notes 
what to_string will do 
{1, 2, 3}
B = ["*", 1, 1, 1]
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
'''
#---------------------------------------------------------------------------------------------------------
B = [] #empty list  
n = int(sys.argv[1]) #gives the size of the inital set 
k = int(sys.argv[2]) #equals the size of the subsets that need to be printed

#B = int(sys.argv[1])
#k = int(sys.argv[2])
#n = len(B)

#---------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------
my_set = {1}
s = 1
for i in range(n):
    my_set.add(s)
    s = s + 1 
my_set = set(my_set)
print("set is = ", my_set)

B = list(my_set) #S 
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

def bitList(n, k):
    if n == 0: 
        return []
    if n == 1: 
        return [str(i) for i in range(0, k)]   
        return [digit + bits for digit in bitList(1, k) for bits in bitList(n - 1, k)]

#def powerset(B)
def to_string(B): #iterative function to print all distinct subsets of S
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

def printSubsets(B, k, i): #prints k-element subsets of any n-element set
    #powerSet(B)
    #if k > n - i + 1: 
        #pass 
    to_string(B)
#---------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------

def main():
    #S = [1, 2, 3]
    #powerSet(S)
    printSubsets(B, k, i)

if __name__ == '__main__':
    main()
    


