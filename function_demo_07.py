#function_demo_07.py

#lambda expressions

#anonymous function

#syntax

# f = lambda x, y, z : x+y*z

fn = lambda x, y, z : 100* x + 10 * y + z

def hoo(x, y, z) :
    return 100*x + 10 * y + z

print(fn(1, 3, 2))
print(hoo(1, 3, 2))

evenp = lambda x : x%2 == 0  #to check if x is even

print(evenp(100))
print(evenp(123))

ls = [('pavithra',62), ('Janith',64),('Hiruni', 60)]

print(ls)
ls.sort()
print(ls)
ls.sort(key = lambda x : x[1])

print(ls)

def get_2nd(tp) :
    return tp[1]
ls = [('pavithra',62), ('Janith',64),('nissan', 60)]
print(ls)

ls.sort(key = get_2nd)

print(ls)


ls1 = [(1,2),(4,6),(3,8),(2,7)]
lss1 = sorted(ls)
lss2 = sorted(ls, key = lambda x : x[1])
lss2r = sorted(ls, key = lambda x : x[1],reverse = True)
