# composite_function
def foo(x):
    return 2*x + 1
def goo(x):
    return 2*x**3

def composite11(f,g):
    def _comp(x):
        return f(g(x))
    return _comp

def plus(x,y):
    return x+y
def sqr(x):
    return x**2
def dist(x,y):
    return x**2+y**2

def composite12(f,g):
    def _comp(x,y):
        return f(g(x),g(y))
    return _comp
    
dist2 = composite12(plus, sqr)

d = dist(3,4)
print(f"{d=}")

d1 = dist2(3,4)
print(f"{d1=}")


def dist3d(x,y):
    return x**3 - y**3

dist3 = composite12(lambda x,y: x-y, lambda x : x**3)

d3d = dist3d(3, 2)

d3 = dist3(3, 2)

print(f"{d3d=}  and {d3=}")
