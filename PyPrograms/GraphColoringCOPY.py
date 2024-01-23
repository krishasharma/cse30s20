#GraphColoringCOPY.py 

#------------------------------------------------------------------------------
# Krisha Sharma 
# krvsharm
# CSE 30-02 Spring 2021
# PA 6
# GraphColoring.py 
# Client program 
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
import sys
from graph import *


def CheckProperColoring(G):
    """
    Return True if no two adjacent vertices in G have like colors,
    False otherwise.
    """

    pass
# end

def main():
    # check command line arguments and open files

    # read each line of input file

    # get number of vertices on first line, create vertex list

    # create edge list from remaining lines

    # create graph G

    # Determine a proper coloring of G and print it to the output file

    if len(sys.argv)!=3:
        usage()
    try:
        infile = open(sys.argv[1])
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        usage()
    

    outfile = open(sys.argv[2], 'w')
    lines = infile.readlines() # read lines put every line in a list

    E = [] # empty list 
    V = []
    v = int(lines[0])
    for j in range(1, v+1):
        V.append(j)
    #print(V) # printing to terminal CHECK 
    for i in range(1, len(lines) - 1):
        str_pair = lines[i]
        edge = str_pair.split(" ") # splitting by tab and makes a list 
        tup = (int(edge[0]), int(edge[1]))
        E.append(tup) 

    G = Graph(V,E)

    cs = set(G.Color())

    print(len(cs), 'colors used:', cs, file=outfile)



    #print(file=outfile)
    #msg = 'coloring is proper: {}'.format(CheckProperColoring(G))
    #print(msg, file=outfile )
    
    infile.close()


    """
    # Check that the coloring is correct
    print(file=outfile)
    msg = 'coloring is proper: {}'.format(CheckProperColoring(G))
    print(msg, file=outfile )
    """
# end

if __name__=='__main__': 
    main()