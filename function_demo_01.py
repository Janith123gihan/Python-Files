#named function_demo_01.py
def welcome() :
    print('Hello')

def welcome_2(name) :
    print('Hello', (name),'welcome to the python')
    print(f"hello {name} welcome to the python")

def welcome_3(name = "john") :#default-valued parametre
    print('Hello',name,'welcome tho the python')
    print(f"Hello {name} welcome to the python")

if __name__ == '__main__' :
    welcome()
    welcome_2('janith')# actual parametre argument
    welcome_3()#no argument is passed
    welcome_3('gihan')


def welcome_3(name:str = 'John') -> None :
    print(f"welcome {name} to my world")
if __name__ == '__main__' :
    welcome_3()
