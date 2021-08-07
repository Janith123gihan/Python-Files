#recursion
#Recursive function
#a function call itself directly or indirectly
#A function A calls A or (A calls B and B calls A)

def _factorial(n) :
    if n==0 or n==1 :
        return 1
    return n * _factorial(n-1)

def factorial_it(n) :
    f = 1
    for i in range(1, n+1) :
        f *= 1
    #end for
    return f

print(_factorial(12))
#print(math.factorial(12))

m = 123

#print(f'from math module {m}! = {math.factorial(m)}')
#print(f'from_factorial {m}! = {_factorial(m)}')
