from typing import List


class Calculus():

    def __init__(self, factor=0, square=0, cube=0, square_root=0):
        self.factor = factor
        self.square = square
        self.cube = cube
        self.square_root = square_root

    def factors(self, x):
        self.factor = 1
        for num in range(1, (x + 1)):
            self.factor = num * self.factor
        return self.factor

    def squares(self, x):
        self.square = x ** 2
        return self.square

    def cubes(self, x):
        self.cube = x ** 3
        return self.cube

    def square_roots(self, x):
        self.square_root = x ** 0.5
        return self.square_root


'''
a = Calculus()
print(a.factors(x))
print(a.squares(x))
print(a.square_roots(x))
print(a.cubes(x))'''

numbers = [42, 73, 0, 16, 10, 6, 18, 24, 31, 65]
is_big = [nums for nums in numbers if nums > 10 ]
print(is_big)
big = [num > 10 and num % 2 != 0 for num in numbers]
print(big)

