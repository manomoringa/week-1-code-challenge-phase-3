
def apply_decorator(func):
    def wrapper(*args, **kwrags):
        print('Decorator applied')
        return func(*args,**kwrags)
    return wrapper
def decorator_func(func):
    return apply_decorator(func)

def day():
    print('today is awesome')

@apply_decorator
def my_function():
    print("Original Function Called")

my_function()