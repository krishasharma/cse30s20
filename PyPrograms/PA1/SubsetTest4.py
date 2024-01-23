#SubsetTest4.py 
import sys
import math
# Program to print all combination
# of size r in an array of size n
 
# The main function that prints all
# combinations of size r in arr[] of
# size n. This function mainly uses
# combinationUtil()

B = int(sys.argv[1]) #gives the size of the inital set 
k = int(sys.argv[2]) #size of subsets 
n = len(B)

def printCombination(B, n, k):
    # A temporary array to store
    # all combination one by one
    data = [0] * k

    # Print all combination using
    # temprary array 'data[]'
    combinationUtil(B, n, k, 0, data, 0)
 
''' 
arr[] ---> Input Array
n     ---> Size of input array
r     ---> Size of a combination to be printed
index ---> Current index in data[]
data[] ---> Temporary array to store
            current combination
i     ---> index of current element in arr[]     
'''

def combinationUtil(B, n, k, index, data, i):
 
    # Current cobination is ready,
    # print it
    if (index == k):
        for j in range(k):
            print(data[j], end = " ")
        print()
        return
 
    # When no more elements are
    # there to put in data[]
    if (i >= n):
        return
 
    # current is included, put
    # next at next location
    data[index] = B[i]
    combinationUtil(B, n, k, index + 1, data, i + 1)
 
    # current is excluded, replace it
    # with next (Note that i+1 is passed,
    # but index is not changed)
    combinationUtil(B, n, k, index, data, i + 1)
 
# Driver Code
if __name__ == "__main__":
    #B = [1, 2, 3, 4, 5]
    #k = 3
    #n = len(B)
    B = int(sys.argv[1]) #gives the size of the inital set 
    B_str = str(B)
    n = len(B_str)
    k = int(sys.argv[2]) #size of subsets 
    printCombination(B, n, k)

'''
# Program to print all combination
# of size r in an array of size n
 
# The main function that prints all
# combinations of size r in arr[] of
# size n. This function mainly uses
# combinationUtil()
def printCombination(arr, n, r):
 
    # A temporary array to store
    # all combination one by one
    data = [0] * r
 
    # Print all combination using
    # temprary array 'data[]'
    combinationUtil(arr, n, r, 0, data, 0)
 
 
#arr[] ---> Input Array
#n     ---> Size of input array
#r     ---> Size of a combination to be printed
#index ---> Current index in data[]
#data[] ---> Temporary array to store current combination
#i     ---> index of current element in arr[]   

def combinationUtil(arr, n, r, index, data, i):
 
    # Current cobination is ready,
    # print it
    if (index == r):
        for j in range(r):
            print(data[j], end = " ")
        print()
        return
 
    # When no more elements are
    # there to put in data[]
    if (i >= n):
        return
 
    # current is included, put
    # next at next location
    data[index] = arr[i]
    combinationUtil(arr, n, r, index + 1,
                    data, i + 1)
 
    # current is excluded, replace it
    # with next (Note that i+1 is passed,
    # but index is not changed)
    combinationUtil(arr, n, r, index,
                    data, i + 1)
 
# Driver Code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    r = 3
    n = len(arr)
    printCombination(arr, n, r)

'''