def apply_callback(callback):
    def decorator(func):
        def wrapper(*args, **kwargs):
            input_list = args[0]
            modified_list = [callback(item) for item in input_list]
            return func(modified_list, *args[1:], **kwargs)

        return wrapper
    return decorator

def square(x):
    return x ** 2

def double(x):
    return x * 2

@apply_callback(square)
def sum_squares(numbers):
    return sum(numbers)

@apply_callback(double)
def sum_doubles(numbers):
    return sum(numbers)

print(sum_squares([1, 2, 3])) 
print(sum_doubles([1, 2, 3]))