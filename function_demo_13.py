#function_demo_13.py

"""
Define a tail-recursive function to find the sum of a list of a integers
"""

def my_sum_it(ls:list) -> int :
    """
        sum(ls) gives the sum of numbers in ls"""
    total = 0
    for i in ls :
        total += i
    #end for

    return total
#end def

def my_sum_list_tr(ls, tsum =0 ) :
    if ls :
        return my_sum_list_tr(ls[1:] , ls[0] + tsum)
    return tsum

print(my_sum_list_tr((40,60,80,70)))
