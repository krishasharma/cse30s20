#QueensTest3.py

# A helper function to print solution
''' A helper function to check if a queen can
be placed on board[row][col]. Note that this
function is called when "col" queens are
already placed in columns from 0 to col -1.
You need to check only left side for
attacking queens '''

result = []
n = int(sys.argv[1])

def placeQueen(B, i, j): 
#def isSafe(board, row, col):
    # Check this row on left side
    for x in range(j):
        if(B[i][x]):
            return False
    #for i in range(col):
        #if (board[row][i]):
            #return False
 
    # Check upper diagonal on left side
    row = i
    col = j 
    #i = row
    #j = col
    
    while row >= 0 and col >= 0:
        if(B[row][col]):
            return False
        row -= 1
        col -= 1
 
    # Check lower diagonal on left side
    row = i
    col = j 
    #i = row
    # = col

    while col >= 0 and row < n:
        if(B[row][col]):
            return False
        row = row + 1
        col = col - 1
 
    return True
 
 
''' A recursive helper function to solve N
Queen problem '''
 
# Solves N queen puzzle 
def solveNQUtil(board, col): # solves NQ until a base case #def findSolutions(B, i, mode)

    ''' base case: If all queens are placed
    then return true '''
    if (col == n):
        v = []
        for i in board:
          for j in range(len(i)):
            if i[j] == 1:
              v.append(j+1)
        result.append(v)
        return True
 

    res = False
    for i in range(n):
 
        ''' Check if queen can be placed on
        board[i][col] '''
        if (isSafe(board, i, col)):
 
            # Place this queen in board[i][col]
            board[i][col] = 1
 
            # Make result true if any placement
            # is possible
            res = solveNQUtil(board, col + 1) 
 
            ''' If placing queen in board[i][col]
            doesn't lead to a solution, then
            remove queen from board[i][col] '''
            board[i][col] = 0  # BACKTRACK
 
    ''' If queen can not be place in any row in
        this column col then return false '''
    return res
 
 
''' Uses Backtracking. It mainly uses solveNQUtil() to
solve the problem. It returns false if queens
cannot be placed, otherwise return true and
prints placement of queens in the form of 1s.'''
 
 
def solveNQ(n):
    result.clear()
    board = [[0 for j in range(n)]
             for i in range(n)]
    solveNQUtil(board, 0)
    result.sort()
    return result
 

def main(): 
    n = 8
    res = solveNQ(n)
    print(res)

if __name__ == '__main__': 
    main()




