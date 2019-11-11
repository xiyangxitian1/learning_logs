import random


def double_values(*nums):
    """返回最大与最小值"""
    print(nums)
    return max(nums), min(nums)


# print(*double_values(*[random.randint(10, 20) for _ in range(10)]))
# 列表解析


def triangle_show(n):
    tail = " ".join([str(i) for i in range(n, 0, -1)])
    width = len(tail)
    for i in range(1, n):
        print(
            "{:>{}}".format(" ".join([str(j) for j in range(i, 0, -1)]), width))
    print(tail)


# triangle_show(12)

