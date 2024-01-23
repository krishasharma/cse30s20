#------------------------------------------------------------------------------------------------------
#  BinaryConversionExercise.py
#------------------------------------------------------------------------------------------------------
import math 
import sys 

n = int(sys.argv[1])
b = int(sys.argv[2])
'''
def printBinary1(n):
   """Prints the binary digits of n, in wrong order"""
   while n>0:
      print(n%b, sep='',end='')
      n = n//b
   # end
# end

def printBinary2(n):
   """Prints the binary digits of n, in correct order"""
   L = []
   while n>0:
      L.append(n%b)
      n = n//b
   # end
   L.reverse()
   for digit in L: 
      print(digit, sep='', end='')
   # end
# end

def printBinary3(n):
   """Recursively prints the binary digits of n, in wrong order"""
   if n>0:
      print(n%b, sep='',end='')
      printBinary3(n//b)
   # end
# end
'''
def printBinary4(n):
   """Recursively prints the binary digits of n, in correct order"""
   if n>0:
      printBinary4(n//b)
      print(n%b, sep='',end='')
   # end 
   else: 
       return n%b
# end
#-----------------------------------------------------------------------------------------------------

def main():
    print(printBinary4(n))

if __name__=='__main__':
    main() 
#end 


