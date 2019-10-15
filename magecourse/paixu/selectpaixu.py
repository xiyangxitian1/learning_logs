from random import randint
from datetime import datetime


def sort(arr):
    """选择排序"""
    minIndex = 0
    length = len(arr)
    for i in range(length - 1):
        minIndex = i
        for j in range(i + 1, length):
            if arr[minIndex] > arr[j]:
                minIndex = j
        if minIndex != i:
            temp = arr[minIndex]
            arr[minIndex] = arr[i]
            arr[i] = temp


# lst = [3, 4, 9, 8, 7, 6, 1]
# sort(lst)
# print(lst)


lst = [randint(1, 1000000) for i in range(100000)]
start = datetime.now()
sort(lst)
end = datetime.now()
s = (end - start).seconds
print("use time is {}s".format(s))  # 这个排序也是超级慢的，在数据量很少的时候可以使用
