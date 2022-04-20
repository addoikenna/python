print("This is a python file")

'''
A program that takes an input and outs the factorial of the number
'''
from fun import factor, cube
import math
from calcus import Calculus

while True:
    try:
        x = int(input("Enter a number:\n"))
    except:
        print("Invalid!!! Please enter a number")
    else:
        break
factor(x)

print(math.factorial(16))

cube(x)

a = Calculus()
print(a.factors(x))
print(a.squares(x))
print(a.square_roots(x))
print(a.cubes(x))

