#Lab2.py 
#------------------------------------------------------------------------------
# Krisha Sharma 
# krvsharm
# CSE 30-02 Spring 2021
# Lab 2
# Subset.py 
# description of program 
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#start functions

#L replaces B

def to_string(L): #bit list converts to subset
    if len(L) == 0: 
        return "{ }"

    flag = 0 
    a = []
    for point, flag in enumerate(L):
        a.append(point)
    #remove = str(L)[1:-1]
    return ('{}'.format(L)).replace('[','{').replace(']','}')
    

def printSubsets(L, n, k, i):
    #if k == 0: 
        #print("{ }")
    #elif k == 0: 
        #print(to_string(L))       
    if k == 0: #call to_string
        print(to_string(L))
        
    elif k > n - i + 1:
        return 
    else:
        L.append(i)
        printSubsets(L, n, k-1, i+1) 
        L.pop(-1) #pop
        printSubsets(L, n, k, i+1)

def usage():
    print("Usage: python3 Subset.py n k (where 0<=k<=n)", file=sys.stderr)
    exit()

'''
def usage():
   print("Usage: $ python3 Copy.py [-o <output file>] file1 file2 ..", file=sys.stderr)
   exit()
'''

#end
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#driver code  

'''
def main(): 
    if len(sys.argv)==1:
        usage()
    elif sys.argv[1]=="-o" and len(sys.argv)==2:
        usage()
    elif sys.argv[1]=="-o":
        out = open(sys.argv[2], 'w')  # open file in mode 'w' write
        files = sys.argv[3:]
    else:
        out = sys.stdout
        files = sys.argv[1:]
   # end

    s = ""
    for name in files:
        try:
            f = open(name)  # default open mode is 'r' read
        except FileNotFoundError as e:
            print(e, file=sys.stderr)
            usage()
      # end

        content = f.read()  # reads entire file as one string
        s += content
   # end

   # now print everything to output file or to stdout
    print(s, file=out)

# end
'''

if __name__ == '__main__':

    import math 
    import sys 
    L = []
    try: 
        #if len(sys.argv) == 1:  
            #exit()
        #if len(sys.argv) == 3:
            #errorStatements()
        #if len(sys.argv) == str:
            #print(errorStatements())
        
        if len(sys.argv) != 3: 
            #print("Usage: python3 Subset.py n k (where 0<=k<=n)")
            usage()
            exit()

        if sys.argv[1].isnumeric() == False:
            print("cannot parse \'" + sys.argv[1] + "\' as int", file=sys.stderr)
            usage()

        if sys.argv[2].isnumeric() == False:
            print("cannot parse \'" + sys.argv[2] + "\' as int", file=sys.stderr)
            usage()

        n = int(sys.argv[1])
        k = int(sys.argv[2])
    
        if n < k: 
            usage()



        #if len(sys.argv) == 1 or len(sys.argv) == 2: #if the first command line argument is just a string print the error statements 
            #errorStatements()
        if k == 0: 
            print("{ }")
        else: 
            printSubsets(L, n, k, 1)

    
        
    except ValueError:
        exit()
#end 
#------------------------------------------------------------------------------