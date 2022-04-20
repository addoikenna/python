def new_decorator(original_func):

    def wrap():
        print('This is 1')
        original_func()
        print('This is 2')
    return wrap

@new_decorator
def sim():
    print(f'This is my name function')

#a = new_decorator(sim)
sim()
#a()