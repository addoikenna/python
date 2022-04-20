'''
Fibonnacci sequence
A program that calculates the fibonacci sequence of a given number
'''

#using a generator function
def fibonnaci(n):
    x = 0
    y = 1
    for num in range(n):
        yield x
        x, y = y, x + y
#the try and except will ensure that only numerical inputs are accepted
try:
    n = int(input('Enter a number: '))
    for x in fibonnaci(n):
        print(x)
except:
    print("Invalid!!! Please enter a number")

#without a function
a = 0
b = 1
n = int(input("Enter a number: "))
for num in range(n):
    print(a)
    c = a + b
    a = b
    b = c
