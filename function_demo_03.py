#function_demo_03.py
from function_demo_02 import * #import all what we defined in function_demo_02.py

def person_details(name : str ,age :int) -> None :
    print(f"Person is {name} and of age {age}")
