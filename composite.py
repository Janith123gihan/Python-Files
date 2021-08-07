#Composite.py

def foo(x):
    return 2*x + 1
def goo(x):
    return 2*x**2 - 3

h3 = foo(goo(3))

k5 = goo(foo(5))

print(3,h3)
print(5,k5)

"""def composite(f,g):
    def _comp(*x):
        return f(g(*x))
    return _comp
"""
def plus(x,y):
    return x+y

def sqr(x):
    return x**2

def composite12(f,g):
    def _comp(x,y):
        return f(g(x), g(y))
    return _comp



dist2 = composite12(plus,sqr)
d = dist2(3,4)
print(f"{d=}")

dist3 = composite(lambda x,y : x-y, lambda x : x**3)

d31 = dist3d(3,2)

d3 =  dist3(3,2)

print(f"{d3d=} and {d31=}")
