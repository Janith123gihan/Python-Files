#function_demo_16.py
'''
global

'''
gv1 = 100
gv2 = 200

def fun1():
    global gv1

    gv2 = 345

    print(f"within fun1 gv1 = {gv1} and gv2={gv2}")

    gv1 = 123
    gv2 = 999 

    print(f"within fun1 gv1 = {gv1} and gv2 = {gv2}")
#end def

print(f"Outside fun1: gv1 = {gv1} and gv2 = {gv2}")
fun1()
print(f"Outside fun1: gv1 = {gv1} and gv2 = {gv2}") 
