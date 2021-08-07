#function_demo 02.py

from function_demo_01 import welcome_3 as wel3


def celcius_to_fahrenheit(c : float = 0) -> float :
     f = 9/5 *c +32
     return f

def fahrenheit_to_celecius(f : float = 0) -> float :
    c = (f-32)* 5/9

    return c
