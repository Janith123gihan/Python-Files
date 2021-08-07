#factorial

def factorial(n) :
    if n == 1 or n == 0 :
        return 1
    
    if n > 1 :
        ir = factorial(n-1)
        res = n * ir
        return res
    
    return -1
    
print(factorial(3))

def factorial_tr(n,f=1) :
    if n == 0 or n == 1 :
        return f
    if n > 1 :
        return factorial_tr(n-1, n*f)
    return -1



print(factorial_tr(5,1))


def my_rev_list(ls:list)-> list :
    """returns a list of elements of ls but reverse order"""
    n = len(ls)
    if n==0 or n==1 : return ls
    if n > 1 :
        h = ls[0]
        rev = my_rev_list(ls[1:])
        rev.append(h)
        return rev
    return -1
#end def

ls = list('PYTHON')
print(my_rev_list(ls))

def my_rev_list_tr(ls, nls = None) :
    if nls == None :
        nls = []
    if ls == [] :return nls
    
    h = ls[-1]
    nls.append(h)
    return my_rev_list_tr(ls[:-1], nls)
#end def

ls = list('PYTHON')
print(my_rev_list(ls))    
