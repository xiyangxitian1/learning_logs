from random import randint


def mergingSort(*arr):
    """归并排序"""
    arr0 = arr[0]
    if len(arr0) == 1:
        return arr0
    num = len(arr0) >> 1
    leftArr = arr0[:num]
    rightArr = arr0[num:]
    # print("split lef: " + str(leftArr) + " right: " + str(rightArr))
    return mergingArr(mergingSort(leftArr), mergingSort(rightArr))


def mergingArr(*arr):
    """归并列表"""
    arr1 = arr[0]
    arr2 = arr[1]
    i, j, k = 0, 0, 0
    # result = [0 for i in range(len(arr1) + len(arr2))]
    result = [0] * (len(arr1) + len(arr2))
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result[k] = arr1[i]
            i += 1
        else:
            result[k] = arr2[j]
            j += 1
        k += 1
    while i < len(arr1):
        result[k] = arr1[i]
        k += 1
        i += 1
    while j < len(arr2):
        result[k] = arr2[j]
        k += 1
        j += 1
    return result


lst = [randint(1, 10) for i in range(1000000)]
print("begin")
lst = mergingSort(lst)
print("ok")
