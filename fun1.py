#functiondemo1.py

def welcome() :
    print('Hello')

def welcome_2(name) :
    print('Hello', (name),'welcome to the python')
    print(f"hello {name} welcome to the python")

def welcome_3(name = "john") :#default-valued parametre
    print('Hello',name,'welcome tho the python')
    print(f"Hello {name} welcome to the python")



welcome()
welcome_2('janith')# actual parametre argument
welcome_3()#no argument is passed
welcome_3('gihan')
