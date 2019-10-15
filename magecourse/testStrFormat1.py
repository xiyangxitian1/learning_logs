num = input("请输入一个数字:").strip().lstrip("0")

print("这是一个{}位数字".format(len(num)))

for i in range(len(num)):
    print("{} 出现了 {} 次".format(num[len(num) - i - 1], num.count(num[len(
        num) - i - 1])))
