'''
Factorial of a any given number
'''
print("PROGRAM THAT CALCULATES THE FACTORIAL OF A GIVEN NUMBER")
#using a function

def factorial(num):
    count = num
    product = 1
    while count > 0:
        product = product * count
        count -= 1
    return product

try:
    num = int(input("Enter a number: "))
    x = factorial(n)
except:
    print("Invalid input!!! Please enter a number.")
print(f"The factorial of {n} is {x}")

