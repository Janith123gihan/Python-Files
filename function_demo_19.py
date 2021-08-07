#function_demo_19.py

#generator - example

from itertools import permutations

"""

import itertools
permutations = itertools.permutations
"""

perms = permutations('abc',2) #('a','b','c')

for p in perms:
    print(p)

def my_permutations_gen(ls):
    ln = len(ls)
    if n < 2:
        yield ln
    else:
        a = ls[0]
        gen1 = my_permutations_gen(ls[1:])

        for pm in gen1:
            for i in range(len(pm)):
                pm_cpy = pm[:]
                pm_cpy.insert(i, a)
                yield pm_cpy.insert(i,a)
                yield pm_cpy
            #end for
        #end for

genp = my_permutations_gen('abc')

for i in genp:
    print(i) 
