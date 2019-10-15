from datetime import datetime
from random import randint


def sort(nums):
    """冒泡排序"""
    length = len(nums)
    # 设置标志，如果一次没有交换就退出  因为说明是已经排序好的了
    flag = False
    count_swap = 0
    count = 0
    for i in range(length):
        flag = False
        for j in range(length - i - 1):
            count += 1
            if nums[j] > nums[j + 1]:
                count_swap += 1
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
                flag = True
        if not flag:
            break


lst = [randint(1, 1000000) for i in range(1000000)]
start = datetime.now()
sort(lst)
end = datetime.now()
s = (end - start).seconds
print("use time is {}s".format(s))  # 需要时间超长
