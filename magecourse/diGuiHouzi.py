import datetime
sum = 0


def houzi(n):
    """
    用递归的方法来解决猴子原来有多少桃子
    :param n:
    :return:
    """
    if n == 10:
        return 1
    else:
        return (houzi(n + 1) + 1) * 2

start = datetime.datetime.now()
print(houzi(1))
end = datetime.datetime.now()
print((end-start).microseconds)
