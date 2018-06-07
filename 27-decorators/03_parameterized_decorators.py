def accepts(*types):
    def decorator(f):
        def wrapper(*args, **kwargs):
            if len(args) != len(types):
                raise Exception("Invalid Args: expected {} got {}".format(len(types), len(args)))

            for a, t in zip(args, types):
                if type(a) != t:
                    raise Exception("Invalid arg: {}".format(a))

            return f(*args, **kwargs)
        return wrapper
    return decorator

@accepts(int, int)
def two_x_and_y(x, y):
    return 2 * x + y


print(two_x_and_y(2.5, 3))