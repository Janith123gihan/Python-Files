 #function_demo_08.py

#function tha returns a function

def get_mod_n(n) :
     return lambda x : x % n

mod7 = get_mod_n(7)

mod11 = get_mod_n(11)

mod5 = get_mod_n(5)


def get_inc_n(n) :
    return lambda x : x + n

inc1 = get_inc_n(1)
inc3 = get_inc_n(3)

dec1 = get_inc_n(-1)

mod7 = lambda z : z % 7


#function that another function as an argument


def pretty_print(f) :
    def _print(*args) :
        v = f(*args)
        print('=========================')
        print(v)
        print('=========================')
    return _print

def foo(x) :
    return x + 10

def goo(x,y) :
    return x**2 + y**2

def hoo(x, y, z) :
    return 100*x + 10*y + z

print('*' * 20)
print(foo(10),goo(3,4), hoo(3, 1, 2))
print('-' * 20)

foo1 = pretty_print(foo)

goo1 = pretty_print(goo)

hoo1 = pretty_print(hoo)

foo1(10)

goo1(3,4)

hoo1(3, 1, 2)

print()
print('^' * 20)

foo = pretty_print(foo)

goo = pretty_print(goo)

hoo = pretty_print(hoo)

foo(10)

goo(3,4)

hoo(3, 1, 2)


print('*' * 20)
print(foo(10),goo(3,4), hoo(3, 1, 2))
print('-' * 20)































