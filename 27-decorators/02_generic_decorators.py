def debug(f):
    def wrapper(*args, **kwargs):
        print(f"--- Got arguments: {args}; {kwargs}")
        res = f(*args, **kwargs)
        print(f"--- return value: {res}")
        return res
    return wrapper

def twice(x):
    return x * 2

def thrice(x):
    return x * 3

print(twice(10))
