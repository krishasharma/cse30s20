#Quiz1Question1.py 
def F(n):
    #begin solution 
    if n<0:
        print("your input can't be less than 0")
    elif n==0: 
        return 0 
    elif n==1:
        return 1
    else:
        return F(n-1)+F(n-2)
    #end solution 

    
#driver code
print(F(56))

