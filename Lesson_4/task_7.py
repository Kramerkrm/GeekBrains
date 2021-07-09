from itertools import count
from math import factorial

def fibo_gen():
    for el in count(1):
        yield factorial(el)

z = 0
for el in fibo_gen():
    if z == 10:
        break
    else:
        z += 1
        print(f'Factorial {z} = {el}')
