#------------------------------------------------------------------------------
# Krisha Sharma 
# krvsharm
# CSE 30-02 Spring 2021
# PA 4
# ContinuedFractions.py
# contains a recursive function CF(L) that takes as input a list of ints L, 
# then returns a Rational object representing the rational number corresponding 
# to the continued fraction given by L.
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
from rational import *
from decimal import *
import sys

def CF(L): 
    numer = int(L[-1])
    denom = 1
    finalresult = Rational(numer, 1) #initilize to zero
    L.pop(-1)
    for k in L[-1::-1]: 
        numer = int(L[-1])
        current = Rational(numer, 1)
        finalresult = current + finalresult.inverse() #calling Ration class inverse
        L.pop(-1)
    return finalresult 

def usage():
    sys.stderr.write("Usage: $ python3 ContinuedFractions.py <input file> <output file>")
    exit()


def main():
    # check command line arguments and open files
    if len(sys.argv)!=3:
      usage()
   # end
    try:
        infile = open(sys.argv[1])
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        usage()
   # end
    outfile = open(sys.argv[2], 'w')

   # read in each line of infile, reverse it, then print to outfile
    lines = infile.readlines()
    print("", file=outfile)
    for S in lines:
        L = S.split()
        res = CF(L)
        #print() #blank line 
        getcontext().prec = 100 #setting percision to 100
        print(res, file=outfile)
        print(Decimal(res.numer)/Decimal(res.denom), file=outfile)
        print("", file=outfile)
        #L.reverse()
        #R = ' '.join(L)
    #print("", file=outfile)
   # end

    infile.close()
    outfile.close()

if __name__=='__main__': 
   main()


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


