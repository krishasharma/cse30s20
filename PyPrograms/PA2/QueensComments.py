#QueensComments.py




#-----------------------------------------------------------------------------------------------------------------------------------
'''


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
 
# Solves N queen puzzle 
def solveNQUtil(board, col): # solves NQ until a base case #def findSolutions(B, i, mode)

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
 

        if (isSafe(board, i, col)):
 

            board[i][col] = 1

            res = solveNQUtil(board, col + 1) 
 
            board[i][col] = 0  # BACKTRACK
 
  
    return res
 

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



'''







#-----------------------------------------------------------------------------------------------------------------------------------
'''

B = []
n = int(sys.argv[1])

#i = row 
#k = column 

def place(k, i): #place 
    if (i in B.values()):
        return False
    j = 1
    while(j < k):
        if abs(B[j] - i) == abs(j - k):
            return False
        j += 1
    return True

    
def removeQueen(B, i, j): 
    for i in range()


def NQueens(k): #printing outputs/board 
    for i in range(1, n+1):
        for i in range(k, n+1):
            B[i] = None
        #clear_future_blocks(k)
        if placeQueen(k, i):
            B[k] = i
            if (k == n):
                for j in B:
                    #print(B[j])
                print('---------') #break 
            else:
                NQueens(k+1)


def placeQueen(B, i, j): #creates the queen at a square 
    place(k, i)

def removeQueen(B, i, j):
    clear_future_blocks(k)

#def findSolutions(): #implments the recursion 

def printBoard():
    NQueens(1)

def main(): 
    printBoard()

if __name__ == '__main__': 
    main()

'''
'''
    user = sys.argv[1]
    if user == '-v': 
        val = int(sys.argv[2])
        list = []
        for i in range(val + 1):
            list.append(0)
        B = [list] * (val + 1)
        findSolutions(B, 1, val)
    else:
        user = int(user)
        list = []
        for i in range(user + 1):
            list.append(0)
        B = [list] * (user + 1)
        findSolutions(B, 1, user)   
'''