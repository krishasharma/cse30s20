#SubsetTest2.py

n = int(sys.argv[1])
k = int(sys.argv[2])
set = list(range(n))
B = [] #empty list 

my_set = {1}
s = 1
for i in range(n):
    my_set.add(s)
    s = s + 1 
my_set = set(my_set)
print("set is = ", my_set)
print("set is = ", type(my_set))

#---------------------------------------------------------------------------------------------------------
#used to exit programs if user input is incorrect 
if len(sys.argv) < 3: 
    print("please enter 2 numbers")
    sys.exit()
else: 
    n = sys.argv[1]
    k = sys.argv[2]
    print("argv1 ==> ", n, type(n))
    print("argv2 ==> ", k, type(k))
    try: 
        n = int(sys.argv[1])
        k = int(sys.argv[2])
    except:  
        sys.exit(1) #abort 

if n == "foo" or k == "bar":
    sys.exit()
else: 
    n = int(sys.argv [1])
    k = int(sys.argv[2])
    print('i am here', type(n))
    print(type(k))

print("argv === ", n, type(n))
print("argv === ", k, type(k))
#end 
#---------------------------------------------------------------------------------------------------------
#start of functions 
def bitlist(n, k): #pascals therom, calculates the number of subsets n,k
    if n == 0 or k == n: 
        return 1 
    else: 
        return bitlist(n-1, k) + bitlist(n-1, k-1)
    if n<= k or k < 0 
        return []
    if len(sys.argv) < 3: 
        sys.exit()
    if k == n: 
        return[list(range(k))]
    return bitlist(n-1, k) + [s(n-1) for s in bitlist(n-1, k-1)]

s_list = {}
for i in range(n+1): 
    n = n+1 
    s_list = list(range(n))
    print('===')

def to_string(B): 
#take n  
#make it into a set of numbers in accending order starting at 1 
#creates the numeric n-element set from user input 

#end 

def printSubsets(B, k, i):


def BinCoeff(n, k): #pascals theorm Returns (n choose k), the number of k element subsets of an n-element set.
   if k==0 or k==n: #what if caller has k<0 or k>n?
      return 1
   else:
      return BinCoeff(n-1, k-1) + BinCoeff(n-1, k)
   #end
#end
#---------------------------------------------------------------------------------------------------------
#start of main code 
def main():
    print(BinCoeff(n, k))

if __name__=='__main__':
    main() 

n = 3 
for i in range(n):
    B.append(0)

B[i] = 1 
#end 




'''
# A Python3 program to count number
# of partitions of a set with n
# elements into k subsets
 
# Returns count of different partitions of n elements in k subsets

n = int(sys.argv[1])
k = int(sys.argv[2])

def countP(n, k):
    # Base cases
    if (n == 0 or k == 0 or k > n):
        return 0
    if (k == 1 or k == n):
        return 1
     
    # S(n+1, k) = k*S(n, k) + S(n, k-1)
    return (k * countP(n - 1, k) + countP(n - 1, k - 1))
 
# Driver Code
if __name__ == "__main__":
    print(countP(n, k))
'''

'''
def get_subsets(B): # possibly def to_string(B):
    n = list(B)
    len(n)
    return [[n[k] for k in range(n) if i&1<<k] for i in range(2**n)]
'''
