#Quiz2Question1.py 

def base7digits(n):
    #begin solution
    b = 7
    add = n%b
    if n<=1:
        return str(n)
    else:
        return str(base7digits(n//b)) + str(add)
    #end solution

print(base7digits(10))



