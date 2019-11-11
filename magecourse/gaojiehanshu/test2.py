def compare(a, b) -> bool:
    return a < b


def sort(lst, fn=lambda a, b: a > b):
    """匿名函数"""
    newList = []
    for x in lst:
        for i, y in enumerate(newList):
            if fn(x, y):
                newList.insert(i, x)
                break
        else:
            newList.append(x)

    return newList


lst = [2, 3, 4, 1, 5, 8, 9, 7]
newLst = sort(lst)
print(newLst)
