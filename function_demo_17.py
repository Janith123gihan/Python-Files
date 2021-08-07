#function_demo_17.py

def fun1():

    global gv1

    lx, ly, gv2 = 10, 20, 30

    def fun2():
        nonlocal lx

        lx = 1200
        ly = 2200
        gv2 = 3200

        print("Within function fun2")
        print(f"lx = {lx} ly = {ly} gv1 = {gv1} and gv2 = {gv2}")

    print("within function fun2")
    print(f"lx = {lx} ly = {ly} gv1 = {gv1} and gv2 = {gv2}")

    print("fun2 is called")
    fun2()
    print("fun2 completed")
    print(f"lx = {lx} ly = {ly} gv1 = {gv1} and gv2 = {gv2}")
    gv1 = 9999
    gv2 = 3333

gv1 = 100
gv2 = 200
print("Within Module")
print(f"gv1 = {gv1} and gv2 = {gv2}")
print("fun1 is called")
fun1()
print("fun1 completed")
print(f"gv1 = {gv1} and gv2 = {gv2}")
