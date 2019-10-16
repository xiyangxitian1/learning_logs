def logger(fn):
    def wrap(*args, **kwargs):
        print("before")
        result = fn(*args, **kwargs)
        print("after")
        return result

    return wrap


@logger
def add(x, y):
    print("add")
    return x + y


# sum = logger(add)(3, 4)
print("sum is {}".format(add(3, y=4)))
