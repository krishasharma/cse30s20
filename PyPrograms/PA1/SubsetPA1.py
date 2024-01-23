#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Krisha Sharma 
#krvsharm@ucsc.edu
#Programming Assingment 1 
#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Subset.py 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
my_set = {1}
s = 1
for i in range(n):
    my_set.add(s)
    s = s + 1 
my_set = set(my_set)
#print("set is = ", my_set)
'''
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#start functions
def to_string(B): #bit list converts to subset
    setString = '{' 
    button = 0 #any switch/flag that initializes at 0 
    flag = 0 
    a = []
    for y in B: 
        if y == 1:
            flag += 1 
    if flag == 0:
        return "{ }"
    for point, flag in enumerate(B):
        a.append(point)
    if a == 0: 
        return "{ }"
    for i in range(len(B)): #i is index of bit list
        if B[i] == 1: 
            if(button == 1):
                setString += "," #+= appending for strings 
            setString += str(i) #+= because adding to whats in set string
            button = 1
    setString += "}"
    return setString
    '''
    if k == 0:
        setString = '{ '
        setString += " }"
    return setString
    '''
def printSubsets(B, k, i):
    n = len(B) - 1
    if k == 0: #call to_string
        #print(B)
        print(to_string(B))
    elif k > n - i + 1:
        return 
    else:
        B[i] = 1
        printSubsets(B, k-1, i+1) 
        B[i] = 0 
        printSubsets(B, k, i+1)
#end
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#driver code  
if __name__ == '__main__':
    import math 
    import sys 
    try: 
        if len(sys.argv) == 1:  
            exit()
        if len(sys.argv) == 2:
            exit()
        if len(sys.argv) == str:
            exit()
        n = int(sys.argv[1])
        k = int(sys.argv[2])
        '''
        if k == 0 or k > n: 
            print("{ }")
            exit()
        '''
        #B = list(range(0, n+1))
        B = [0] * (n + 1) 
        B[0] = '*'
        #print(B)
        i = B[1]
        #to_string(B)
        printSubsets(B, k, 1)
    except ValueError:
        exit()
#end 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
try:
    sys.argv1 = sys.argv[:1]+map(int,sys.argv[1:])
    sys.argv2 = sys.argv[:2]+map(int.sys.argv[1:])
except:
    #print 'Incorrect integers', sys.argv[1:]
    exit()
'''




