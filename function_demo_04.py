#function_demo_04.py

#variable number of parametres

def greet(*names) :
    for nm in  names :
        print(f"welcome to {nm} to python function")
#end def
ls = ['Ajanthan','Sobiya','Thilina','Chamodi','Janith']




"""
>>> greet(ls)
(['Ajanthan', 'Sobiya', 'Thilina', 'Chamodi', 'Janith'],)
>>> greet(*ls)
('Ajanthan', 'Sobiya', 'Thilina', 'Chamodi', 'Janith')
"""
def my_sum(*numbers) :  #in here passing number of tuples
    s = 0

    for i in numbers :
        s  += i
    return s
def my_append(ls : list, *items) -> list :
    """
    it gets appended with elements of items
    """
    for e in items :
        ls.append(e)
    return ls


def my_function(p1, p2=3, p4=2, **names) #in here when we initialising named parametres as p2 we should initialise them after initialising un named parametres

"""
>>> ls = ['nimal','chathura']
>>> greet(*ls) #elements of ls are unpacked
welcome to nimal to python function
welcome to chathura to python function
"""
