#function in function
#nested function
#inner-function

def get_power_function(n) :

    def power(p) :
        return n**p

    if n<0 :
        if not isinstance(p, int) :
            raise ValueError
    else:
        return power

#end get_power_function

def get_inc_function(n) :

    def _inc(p):
        return p + n

    return _inc
#end def get_inc_function

def outer(n):

    def p1():
        print("=" * n)

    p1()
    print(n, n**2, n**3)
    p1()

outer(100)
outer(23)
