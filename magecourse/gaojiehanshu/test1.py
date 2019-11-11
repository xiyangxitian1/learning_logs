def counter(base):
    def inc(step=1):
        nonlocal base
        base += step
        return base

    return inc


print(counter(5)())

foo1 = counter(5)
foo2 = counter(2)
print(id(foo1))
print(id(foo2))
