#inc_demo.py

def inc1(x) :
    return x+1

def inc7(x):
    return x+7

def dec2(x):
    return x-2

def gen_inc_fn(n):
    def _inc(x):
        return x + n
    return _inc

inc_1 = gen_inc_fn(1)
inc_7 = gen_inc_fn(7)
dec_2 = gen_inc_fn(-2)

"""
>>> sorted(ls)
[(1, 5), (2, 7), (3, 6), (4, 2), (7, 3)]
>>> sorted(ls, key = lamda x : x[1])
>>> sorted(ls, key = lambda x : x[1])
[(4, 2), (7, 3), (1, 5), (3, 6), (2, 7)]
>>> sorted(ls, key = lambda x : x[0])
[(1, 5), (2, 7), (3, 6), (4, 2), (7, 3)]
>>> sorted(ls, key = lambda x : x[0] + x[1])
[(1, 5), (4, 2), (3, 6), (2, 7), (7, 3)]
>>> sorted (ls, key = lambda x : x[0] - x[1])
[(2, 7), (1, 5), (3, 6), (4, 2), (7, 3)]
>>> sorted (ls, key = lambda x : x[1] - x[0])
[(7, 3), (4, 2), (3, 6), (1, 5), (2, 7)]
>>> sorted (ls, key = lambda x : abs(x[0] - x[1]))
[(4, 2), (3, 6), (1, 5), (7, 3), (2, 7)]
"""
