import math

"""
打印杨辉三角形
    1
  1 1
 1 2 1
1 3 3 1
1 4 6 4 1
第n行有n个数
第n和的和是2**(n-1)
"""
# 计算了一半数的杨辉三角，然后把另一半给补齐
triangle = [[1]]
n = 6
for i in range(n):
    pre = triangle[-1]
    cur = [1]
    for j in range(math.ceil(i / 2)):
        cur.append(pre[j] + pre[j + 1])
    if i % 2 == 0:
        r_temp = cur.copy()
        r_temp.reverse()
        cur += r_temp
    else:
        temp = cur.copy()
        temp.pop(-1)
        temp.reverse()
        cur += temp
    triangle.append(cur)

print(triangle)
