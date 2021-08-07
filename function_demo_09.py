#function_demo_09.py

#decorator_function_pretty_print

def pretty_print(f) :
    def _print(*args) :
        v = f(*args)
        print('=========================')
        print(v)
        print('=========================')
    return _print

@pretty_print
def foo(x) :
    return x + 10

@pretty_print
def goo(x,y) :
    return x**2 + y**2

@pretty_print
def hoo(x, y, z) :
    return 100*x + 10*y + z

foo(10)

goo(3,4)

hoo(3, 1, 2)
