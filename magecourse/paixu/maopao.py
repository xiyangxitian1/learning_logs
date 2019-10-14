num_list = [
    [2, 1, 3, 6, 5, 4, 9, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
]

nums = num_list[0]
# nums = num_list[1]
# nums.reverse()
print(nums)
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

print(nums, count, count_swap)
