#function_demo_06.py

i = 10

def foo (p = i) :
    print(f'Within foo {p=}')

#end def

foo(123)        #Within foo p=123

foo()           #Within foo p=10      

i=100           #Within foo p=10

foo()           #Within foo p=1234

foo(1234)

""" 
after assign default value we can't change it
we can't change 10 as 100

>>> foo.__defaults__
(10,)
>>> foo.__defaults__=(999,)
>>> foo()
Within foo p=999
>>>

here is a method to change defaults but it is
used in developers level not user level

"""

def goo(p, L= []) :
    """
goo append p to l
and return l
"""
    L.append(p)

    return L
#end def

ls = [1, 2, 3]
print(goo(4, ls))
print(goo(33,ls))

"""
>>> goo(100)
[100]
>>> goo(10)
[100, 10]
>>> goo(1000)
[100, 10, 1000]

in here l[] has no default value so it takes as null then p has value 10
so after executing l[] takes default as 10
then again we are calling l[] takes default values


"""









def goo2(p, L = None) :
    if L == None :
        L =[]               #if L==None it will return list is null
    L.append(p)
    return L
#end def

ls = [1,2,3]
print(goo2(4,ls))

print(goo2(33,ls))

print(goo2(10))
print(goo2(100))
print(goo2(1000))
