def show(name, pwd, **kwargs):
    print("name={},pwd={}".format(name, pwd))
    print(kwargs)
    for k, v in kwargs.items():
        print("{}={}".format(k, v))


# show(name="wanger", pwd="123", path='www.baidu.com')

# show("a", "b")

def show1(name, *args, **kwargs):
    print("name={}".format(name))
    print(args)
    for k, v in kwargs.items():
        print("{}={}".format(k, v))


# show1("aa", 1, 2, 3, 4, age=28)

def show2(*args, x, y, **kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)
    for k, v in kwargs.items():
        print("{}={}".format(k, v))


# show2(3, 4, z=7, x=5, y=6)


def show3(x, **kwargs):
    print(x)
    print(kwargs)


# show3(7, j=4, z=4, y=5)

def show4(z, *, x, y, **kwargs):
    print(z)
    print(x)
    print(y)


# show4(8, y=7, x=1

def show5(*args, x=5):
    print(x)
    print(args)


def show6(y, *args, x=5, **kwargs):
    print(y)
    print(args)
    print(x)
    print(kwargs)


# show6(6, 3, 4, z=7, x=8)
