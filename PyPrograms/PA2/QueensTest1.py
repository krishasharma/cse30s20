QueensTest.py 

import sys 
import math 

#i = rows
#j = columns 
#n = queens and size of n x n board 
#B = empty list 

def Queens: 

    def placeQueen(B, i, j): 
        count = 0
        for r in range 1: #for r in range something 
            r <= B.length
            r += 1
            if r < B.length:
                if B[i][r] == 0: 
                    B[i][0] = r
                    B[i][r] = 1
                    if i == B.length - 1: 
                        printBoard(B)
                        return
                    
                    for k in range i + 1: 
                        k < B.length
                        k += 1) 
                        B[k][r] = B[k][r] - 1
                    
                    for x in range 1:
                        x < B.length 
                        x += 1
                        if i + x < B.length and r + x < B.length: 
                            B[i + x][r + x] = B[i + x][r + x] - 1
                        
                    
                    for x in range 1:
                        x < B.length
                        x += 1
                        if i - x < B.length and r - x < B.length: 
                            B[i - x][r - x] = B[i - x][r - x] - 1
                        
                    
                    placeQueen(B, i += 1, 1)
                    removeQueen(B, i-= 1, 0)
                
                count += 1
            

        
        if count < 1: 
            removeQueen(B, i -= 1, 0)
        


    def removeQueen(B, i, j):
        x = B[i][j]

    
    def printBoard(B):
        print("(")
        for j in range 1:
            j < B.length
            j += 1)
            if j != 4:
                print(B[0][j] + ", ")
            
            else:
                print(B[0][j] + ")")
            
        
    def findSolutions(B, i, mode){
        #mode = verbose  
        n = 0
        if(mode == ("-v") == 0)
            while i < B.length: 
                placeQueen(B, i,1)
                i += 1
            
        return n
    
#--------------------------------------------------------------------------------------------

    def main(String[] args) {
            if(args.length < 1) {
                System.out.println("Usage: Queens [-v] number");
                System.exit(1);
            }
            int n;
            if(args[0].compareTo("-v") == 0){
                int[][] B = new int[Integer.parseInt(args[1]) + 1][Integer.parseInt(args[1]) + 1];
                findSolutions(B, 1, args[0]);
            } else {
                int[][] B = new int[Integer.parseInt(args[0]) + 1][Integer.parseInt(args[0]) + 1];
                findSolutions(B, 1, "");
            }
    }

}

