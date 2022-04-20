

def num(n):
    a = 0
    b = 1
    for x in range(n):
        yield a
        a, b = b, a + b
for y in num(3):
    print(y)

def simple_gen():
    for x in range(5):
        yield x

#for number in simple_gen():
 #   print(number)

#a = simple_gen()
#print(next(a))
#print(next(a))
#print(next(a))

'''
A python code that generates the square of numbers up to N 
'''
def square_gen(n):
    for num in range(n):
        yield num ** 2

a = [x for x in square_gen(10)]
print(a)

'''
Create a genertor that yields 'n' random numbers between a low and high (that are inputs)
'''
import random

def randnum(low, high, n):

    for num in range(n):
        yield random.randint(low+1, high-1)
#used the + and - because i want to exclude the low and high
a = [num for num in randnum(1, 10, 5)]
print(a)

'''
Use the iter() function to convert a string into an iterator
'''

s = 'This string is an iterator'

h = iter(s)

print(next(h))
print(next(h))
print(next(h))
print(next(h))

'''
The yield statement in generators returns a result once in is called upon, it does not store the result in the memory.
The return statement in a function holds the result of that function and keeps it to memory 
'''

'''
Generator comprehension 
The gencomp below is a generator 
'''
my_list = [1, 2, 3, 4, 5]
gencomp = (item for item in my_list if item > 3)
print(type(gencomp))

for item in gencomp:
    print(item)