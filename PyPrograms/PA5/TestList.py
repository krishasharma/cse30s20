#------------------------------------------------------------------------------
#  TestList.py
#  A weak test of the List class.
#------------------------------------------------------------------------------
from list import *
from decimal import *

def main():
    #remove
    L = List() 
    L.append(1)
    L.append(2)
    L.append(3)
    L.append(4)
    L.append(5)
    print(L.remove(1)) 

    #reverse 

    #L = List([1, 2, 3])
    #print(L) # => [1, 2, 3]
    #L.reverse()
    #print(L) # => [3, 2, 1] 
    #L = List([8, 16, 52, 17])
    #print(L.reverse())

    L = List([8, 16, 52, 17])
    List.reverse(L)
    print(L)
    
    #getitem
    L = List() 
    L.append(1)
    L.append(2)
    L.append(3)
    L.append(4)
    L.append(5)
    print(L.__getitem__(3))

    #setitem
    L = ([1, 2, 3, 4, 5])
    L.__setitem__(3, 5) 
    print(L)

    #add
    L = List([1, 2, 3, 4, 5])
    L2 = List([1, 2, 3, 4, 5])
    print (L + L2)

    #iadd
    L = List([1, 26, -6, 8, 5])
    L2 = List([59, 4, 91, 8])
    L = L + L2
    L += L2
    print(L)

    #mul
    L = List([1, 2, 3, 4, 5])
    L2 = List([1, 2, 3, 4, 5])
    print(L * 2) 

    #rmul
    L = List([1, 2, 3, 4, 5])
    L2 = List([1, 2, 3, 4, 5])
    print(2 * L)


    
    
    '''
    print(L)
    L = List([1, 2, 3, 4, 5]) #add
    L2 = List([1, 2, 3])
    L += L2
    print(L + L2)
    print(L)
    L = List([1, 2, 3, 4, 5])
    L2 = List([1, 2, 3])
    print(L * 3) 
    print(3 * L)
    '''



if __name__=='__main__':

   main()