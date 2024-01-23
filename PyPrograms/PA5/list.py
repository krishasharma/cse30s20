#------------------------------------------------------------------------------
# Krisha Sharma 
# krvsharm
# CSE 30-02 Spring 2021
# PA 5
# list.py
# Definition of the List class, emulating Python's list type. Based on a
# linked-list data structure.
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

class _Node(object):
   """Private _Node type."""

   def __init__(self, x):
        """Initialize a _Node object."""
        self.data = x
        self.next = None
    # end

# end


class List(object):
   def __init__(self, s=None):
        """Initialize self, a List object."""
        self._front = None
        self._back = None
        self._length = 0
        if s:
            for x in s:
                self.append(x)
            # end
        # end
    # end

   def __len__(self):
        """Return the length of self."""
        return self._length
    # end

   def __str__(self):
        """Return a string representation of self."""
        s = '['
        for x in self:
            s += "{}, ".format(repr(x))
        # end
        if len(self)>0:
            s = s[0:-2]+']'
        else:
            s += ']'
        # end
        return s
    # end

   def __repr__(self):
        """Return a detailed string representation of self."""
        return 'list.List('+str(self)+')'
    # end

   def __iter__(self):
        """Return an iterator over self."""
        N = self._front
        while N:
            yield N.data
            N = N.next
        # end
    # end

   def __eq__(self, other):
        """
        Return True if self and other are the same sequence, False otherwise.
        """
        eq = (len(self)==len(other))
        N = self._front
        M = other._front
        while eq and N:
            eq = (N.data==M.data)
            N = N.next
            M = M.next
        # end
        return eq
    # end

   def append(self, x):
        """Add item x to back of List."""
        N = _Node(x)
        if len(self)==0:
            self._front = self._back = N
        else:
            self._back.next = N
            self._back = N
        # end
        self._length += 1
    # end 

   def clear(self):
        """Delete all items from List."""
        self._front = None
        self._back = None
        self._length = 0
    # end 

   def copy(self):
        """Return a (shallow) copy of List."""
        C = List()
        for x in self:
            C.append(x)
        # end
        return C
    # end

   def insert(self, i, x):
        """Add item x at position i of List, where -n<=i<=n and n=len(self)."""
        n = len(self)
        if not isinstance(i, int):
            raise TypeError('insert() index must be integer')
        # end
        if not -n<=i<=n:
            raise IndexError('insert() index out of range')
        # end

        # interpret negative i as position n-|i|
        if i<0: i += n

        # perform insertion
        N = _Node(x)
        if n==0:   # sepcial case: insertion into an empty list
            self._front = self._back = N
        elif i==n: # special case: insertion at the back
            self._back.next = N
            self._back = N
        elif i==0: # special case: insertion at the front
            N.next = self._front
            self._front = N
        else:      # general case: 1<=i<=n-1
            P = self._front
            S = P.next
            for j in range(1, i):
                P = S
                S = S.next
                # end
            P.next = N
            N.next = S
        # end
        self._length += 1
    # end

   def pop(self, i=-1):
        """
        Delete item at position i of List, where -n<=i<=(n-1) and n=len(self).
        """
        n = len(self)
        if not isinstance(i, int):
            raise TypeError('pop() index must be integer')
        # end
        if n==0:
            raise IndexError('cannot pop() empty List')
        # end
        if not -n<=i<=(n-1):
            raise IndexError('pop() index out of range')
        # end

        # interpret negative i as position n-|i|
        if i<0: i += n

        # perform deletion
        if n==1:      # special case: deletion from a 1-element list
            N = self._front
            self._front = self._back = None
        elif i==0:    # special case: delete front element
            N = self._front
            self._front = N.next
            N.next = None
        else:         # general case: 1<=i<=n-1
            P = self._front
            S = P.next
            for j in range(1, i):
                P = S
                S = S.next
                # end
            N = S
            S = N.next
            P.next = S
            N.next = None
            if not S:  # sub-case: delete back element
                self._back = P
            # end
        # end
        self._length -= 1
        return N.data
    # end

   #---------------------------------------------------------------------------
   #  Functions to be added to List for pa5
   #---------------------------------------------------------------------------

   def remove(self, x):
        """
        Delete leftmost occurance of x in List. Raise ValueError if x is not
        contained in self.
        """
        button=0
        n = self._length
        curr = self._front #set to front 
        for i in range(0, n): #i = 1 
            if x == curr.data:
                self.pop(i)
                button+=1
                break
            curr = curr.next
        if button == 0:
            raise ValueError()
        return self 
   # end

   def reverse(self):
        """Reverse the items of List."""
        '''
        L = List() #create new list
        n = L._length #len
        #for k in range(0, n):
        while n >= 1: 
            L.append(k) #append
            k = L.pop(n-1) #pop
            n = L._length
        return L
        '''
        L = List() #create new list
        n = self._length #len
        while n >= 1: 
            k = self.pop(n-1) #pop
            L.append(k) #append
            n = self._length
        return L
        
   # end

   def __getitem__(self, i):
        """
        Return item at position i of self, where -n<=i<=n-1 and n=len(self).
        """
        button = 0 
        n = self._length
        curr = self._front 
        for k in range(0, n):
            if k == i:
                return curr.data
            curr = curr.next 
        curr = self._front 
        for k in range(-n, 0):
            if k == i:
                return curr.data
            curr = curr.next
        if i >= n: 
            raise ValueError()
   # end

   def __setitem__(self, i, x):
        """
        Overwrite item at position i of self by x, where -n<=i<=n-1 and 
        n=len(self).
        """
        button = 0 
        n = self._length
        curr = self._front 
        for k in range(0, n):
            if k == i:
                curr.data = x #instead of returning current data, initalize it as x 
            curr = curr.next 
        curr = self._front
        for k in range(-n, 0):
            if k == i: 
                curr.data = x
            curr = curr.next
        if i >= n:
            raise ValueError()
        if i < -n: 
            raise ValueError()
   # end

   def __add__(self, other):
        """
        Return the concatenation of self with other. This function implements
        the operation self + other.
        """
        final = List()
        s = List(self)
        o = List(other)
        if self._length == 0: 
            return o
        if other._length == 0: 
            return s
        final._length = self._length + other._length 
        s._back.next = o._front
        final._back = o._back 
        final._front = s._front
        return final 
        pass
   # end

   def __iadd__(self, other):
        """
        Replace self by the concatenation of self with other. This function
        implements the operation self += other.
        """
        self = self + List(other)
        return self
        
   # end

   def __mul__(self, n):
        """
        Return the n-fold concatenation of self with self, where n>=0. This
        function implements the operation self*n.
        """
        L = List()
        for n in range(n): 
            s = List(self)
            L += s
        return L 
        pass
   # end

   def __rmul__(self, n):
        """
        Return the n-fold concatenation of self with self, where n>=0, reversing
        the order of self and n. This function implements the operation n*self.
        """
        L = List() #same as mul?
        for n in range(n): 
            s = List(self)
            L += s
        return L 
        pass
   # end

# end
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#  Test the List type
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def main():

   L = List()
   L.append(1)
   L.append(2)
   L.append(3)
   print(len(L))
   print(L)
   print(repr(L))

   A = List()
   A.append(1)
   A.append(2)
   A.append(3)
   print('A==L :', A==L)
   A.append(4)
   print('A==L :', A==L)
   L.append(5)
   print(L)
   print(A)
   print('A==L is', A==L)

   L.clear()
   print(len(L))
   print(L)

   B = A.copy()
   print(B)
   print(repr(B))
   print('A==B :', A==B)
   print('A is B :', A is B)

   print()
   print(B)
   B.insert(0, 'foo')
   print(B)
   B.insert(3, 'bar')
   print(B)
   B.insert(6, 'one')
   print(B)
   B.insert(-2, 'two')
   print(B)
   print(repr(B))
   print(len(B))

   print()
   print(B.pop(0))
   print(B)
   print(B.pop(2))
   print(B)
   print(B.pop(5))
   print(B)
   print(B.pop(-2))
   print(B)
   print(len(B))
   print()

# end

#------------------------------------------------------------------------------
if __name__=='__main__':

   main()

# end