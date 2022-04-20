def factor(x):
    Number_fac = 1

    for num in range(1, (x + 1)):
        Number_fac = num * Number_fac

    print(f"The factorial of {x} is {Number_fac}")

def cube(x):
    square_x = x ** 2
    cube_x = x ** 3
    sqrt_x = x ** 0.5

    print(f"Square of x: {square_x}\nCube of x: {cube_x}\nSquare root of x: {sqrt_x}")