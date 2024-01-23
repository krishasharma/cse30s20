#QueensTest4.py

#Number of queens
print ("Enter the number of queens")
N = int(input())

#chessboard
#NxN matrix with all elements 0
B = [[0]*N for _ in range(N)]

def removeQueen(B, i, j):
    #checking if there is a queen in row or column
    for k in range(0,N):
        if B[i][k]==1 or B[k][j]==1: #board for B
            return True
    #checking diagonals
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if B[k][l]==1:
                    return True
    return False

def placeQueen(B, i, j, n):
    #if n is 0, solution found
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            '''checking if we can place a queen here or not
            queen will not be placed if the place is being attacked
            or already occupied'''
            if (not(removeQueen(i,j))) and (B[i][j]!=1):
                B[i][j] = 1
                #recursion
                #wether we can put the next queen with this arrangment or not
                if placeQueen(n-1)==True:
                    return True
                B[i][j] = 0

    return False
'''
N_queen(N)
for i in board:
    print (i)
'''
#--------------------------------------------------------------------------------------------

def printBoard():
    placeQueen(N)
    for i in B:
        print (i)

def findSolutions(): 
    #N_Queen(N)

    #if n is 0, solution found
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            '''checking if we can place a queen here or not
            queen will not be placed if the place is being attacked
            or already occupied'''
            if (not(removeQueen(i,j))) and (B[i][j]!=1):
                board[i][j] = 1
                #recursion
                #wether we can put the next queen with this arrangment or not
                if placeQeen(n-1)==True:
                    return True
                B[i][j] = 0

    return False

def main():
    print(printBoard())



if __name__=='__main__':
    main()
