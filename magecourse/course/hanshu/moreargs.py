def add(*nums):
    """ 加法 """
    sum = 0
    print(type(nums))
    for x in nums:
        sum += x

    print("sum is {} ".format(sum))


# add(4, 5, 6, )

def showconfig(**kwargs):
    print(type(kwargs))
    for k, v in kwargs.items():
        print("{}={} ".format(k, v))


showconfig(name='liyan', age=28)

