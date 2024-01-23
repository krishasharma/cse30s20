#graphCOPY.py

#------------------------------------------------------------------------------
# Krisha Sharma 
# krvsharm
# CSE 30-02 Spring 2021
# PA 6
# graph.py 
# graph coloring problem 
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# notes/instructions 
# heuristic
# 1. start somewhere
# 2. while some vertex has not been "processed" (whatever that may mean)
# 3.     pick the "best" such vertex 𝑥𝑥 (whatever "best" means)
# 4.     process 𝑥𝑥
# 5.     for each neighbor 𝑦𝑦 of 𝑥𝑥
# 6.         "update" the vertex 𝑦𝑦 (whatever "update" means)

# heuristic is based on reachable() and BFS() discussed in class 

#------------------------------------------------------------------------------
#  Definition of the Graph class.
#------------------------------------------------------------------------------
from queue import Queue
import sys

class Graph(object):
    """Class representing an undirected graph."""
    # _color: a dictionary whose keys are vertices x, and value _color[x], the color of x
    # _ecs: a dictionary whose keys are vertices x, and value _ecs[x], the excluded color set of x
    # the colors determine wether they are adjacent to each other or not
    # get the keys 
    # start a for or while loop to check if the key is in the other vertices list 

    def __init__(self, V, E):
        """Initialize a Graph object."""
        # basic attributes
        self._vertices = list(V)
        self._vertices.sort()
        self._edges = list(E)
        self._adj = {x:list() for x in V}
        self._color = {x:None for x in V} 
        self._ecs = {x:set() for x in V}
        for e in E:
            x,y = tuple(e)
            self._adj[x].append(y)
            self._adj[y].append(x)
            self._adj[x].sort()
            self._adj[y].sort()
        # end
    # end

    @property
    def vertices(self):
        """Return the list of vertices of self."""
        return self._vertices
    # end

    @property
    def edges(self):
        """Return the list of edges of self."""
        return self._edges
    # end

    def __str__(self):
        """Return a string representation of self."""
        s = ''
        for x in self.vertices:
            a = str(self._adj[x])
            s += '{}: {}\n'.format(x, a[1:-1])
        # end
        return s  
    # end      

    def degree(self, x):
        """Returns the degree of vertex x."""
        return len(self._adj[x])
    # end

    def Color(self):
        """
        Determine a proper coloring of a graph by assigning a color from the
        set {1, 2, 3, .., n} to each vertex, where n=|V(G)|, and no two adjacent
        vertices have the same color. Try to minimize the number of colors
        used. Return the subset {1, 2, .., k} of {1, 2, 3, .., n} consisting
        of those colors actually used.
        """

        # start at some vertex 
        # while there are uncolored verticies 
        #   find the best one, call it x 
        #   assign color[x] = smallest color not in ecs[x]
        #   for all y existing in adj[x]
        #       add color x to ecs[y]

        # initializes
        L = set(self._vertices) # list V undiscovered
        colorsUsed = set()
        x = L.pop() 
        color = self._vertices # list of natural integers representing colors assumes that n = k 
        discovered = list()
        discovered.append(x) 
        while len(discovered) != 0: 
            curNode = discovered.pop(0)
            D = self._ecs[curNode] # excluded color set; colors that t cannot be 
            sc = set(color) # copy of color 
            sd = set(D)  
            print(sc)
            print(sd)
            #print(list(sc.difference(sd)) # V?
            #diff = sc.difference(sd)
            self._color[curNode] = min(list(sc-sd)) # all colors - excluded colors = set of possible colors we can use 
            print(min(sc-sd))
            if self._color[curNode] not in colorsUsed:
                colorsUsed.add(self._color[curNode])
            for y in self._adj[curNode]: # for each neighbor 
                self._ecs[y].add(self._color[curNode]) 
                if y in L: # if its still undiscovered 
                    L.remove(y) # move y from undiscovered
                    discovered.append(y) # to discovered put all neighbors in to queue 
                # end
            # end
            # end
        return colorsUsed # return the set of colors used 

    def getColor(self, x):
        """ Return the color of x."""
        return self._color[x]
    # end

    def _find_best(self, L):
        """Return the index of the best vertex in the list L."""
        # here L is your list of verticies 
        # return the "best" vertex in list of L 
        pass
    # end

# end 

        
'''
# CHRISTINE OH
# source node is the name of the node/vertex you start on
ecs[1] = {} # check the source against the excluded colors dic before assigning it a color 
self._colors[1] = 1 # since ecs is empty, you can assign it to 1 
ecs[7].add(1) # then you check the neighbor and add 1 to the set of colors that the neighbor cant be (here 7 is the neighbor of 1, thus seven cannot have the same color as 1)
ColorsUsed = {} # set for the colors that have been used 
# while loop to not process verticies again 
pass
'''
