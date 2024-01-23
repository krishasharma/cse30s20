#-------------------------------------------------------------------------------------------------------------------------------------------------
#Krisha Sharma 
#krvsharm
#CSE 30-02 Spring 2021
#PA 2 
#Queens.py
#-----------------------------------------------------------------------------------------------------------------------------------

import math 
import sys

def placeQueen(B, i, j): 
    n = len(B)-1 
    B[i][j] = 1 
    B[i][0] = j #indicates existence of queen
    for row in range(i+1, n+1): #row check 
        for column in range(1, n+1): #column check 
            if column == j: 
                B[row][column] -= 1 #decrements by 1 // if (i,j) is the square of the queen this accuounts for every square under (i,j)
            else: #diagonal check 
                if abs(i - row)/abs(j - column) == 1: 
                    B[row][column] -= 1 #decrements diagionaly // if (i,j) is the square of the queen this accounts for the right and left diagonals of the square under (i,j)
            
                
def removeQueen(B, i, j): #reverses everything place queens did
    n = len(B)-1
    B[i][j] = 0 
    B[i][0] = 0 
    for row in range(i+1, n+1):
        for column in range(1, n+1):
            if column == j: 
                B[row][column] += 1 #increments by 1
            else: 
                if abs(i - row)/abs(j - column) == 1: 
                    B[row][column] += 1 #decrements diagionaly // if (i,j) is the square of the queen this accounts for the right and left diagonals of the square under (i,j)


def printBoard(B):
    tup = []
    #n = len(B)-1
    for i in range(1, len(B)): #checks the rows form the first row all the way to n 
        #B[i][0] = j #makes sure that j stays in the zero column; takes everything in the 0 row for i in the range of 1 and the length of B
        tup.append(B[i][0])
        #tup += (B[i][0])
    print(tuple(tup))

def findSolutions(B, i, mode): #if i > n (a queen was placed on row n, and hence a solution was found)
    s = 0 #initalize sum 
    #mode = '-v' #initializing verbose mode 
    #B = (n+1) * [(n+1)*[0]]
    #i = len(B) #length of B is the columns of the board 
    if i > len(B) - 1: 
        if mode == '-v': #if we are in verbose mode
            printBoard(B) #print that solution
        return 1 
    else: 
        for square in range(1, len(B)): #for each square on row i where square is the spot of queen, ignoring the zero column 
            if B[i][square] == 0: #if that square is safe
                placeQueen(B, i, square) #place a queen on that square
                s += findSolutions(B, i+1, mode) #recur on row (i + 1), then add the returned value to an accumulating sum
                removeQueen(B, i, square) #remove the queen from that square
        return s #return the accumulated sum

def errorStatements():
    print("Usage: python3 Queens.py [-v] number")
    print("Option: -v verbose output, print all solutions")

def main(): 
    if len(sys.argv) == 3: #verbose
        mode = sys.argv[1]
        n = int(sys.argv[2])
        B = []
        for x in range(n + 1):
            B.append([0]*(n+1))
        #print(B)
        i = 1
        #print(findSolutions(B, i, mode))
        print(str(n)+"-Queens has "+ str(findSolutions(B, i, mode))+" solutions")

    if len(sys.argv) == 1 or len(sys.argv) == 2: #if the first command line argument is just a string print the error statements 
        errorStatements()
    

    #if len(sys.argv) ==1 and if : 
        #print(str(n)+"-Queens has "+ str(findSolutions(B, i, mode))+" solutions")
        #if len(sys.argv) == 2: #if the second command line argument is just an integer, print n-Queens.py has ____ solutions
            #n = int(sys.argv[1])
            #print(n, "-Queens.py has ____ solutions")
        
if __name__ == '__main__': 
    main()
