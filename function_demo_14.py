#function_demo_14.py

#Recursive function is easy to design, and write
#may not be assigned

def fibonacci_it(n) :
    """0 1 1 2 ....
"""
    if n==0 : return 0
    if n==1 : return 1
    if n>1 :
        f0, f1 = 0, 1
        for i in range(2, n+1) :
            f2 = f1 + f0
            f0, f1 = f1,f2
        return f2
#end def

fib_series10 = [fibonacci_it(i) for i in range(11)]


def fibonacci_ntr(n) :
    """
        f(n) = f(n-1) + f(n-2) for n > 1
        f(0) = 0; f(1) = 1
        """

    if n == 0 or n == 1 : return n

    return fibonacci_ntr(n-1) + fibonacci_ntr(n-2)


def fibonacci_tr(n, fn_2=0, fn_1=1) :
    if n==0 : return fn_2
    if n==1 : return fn_1
    return fibonacci_tr(n-1, fn_1, fn_2 + fn_1)

print([fibonacci_tr(1023)])
