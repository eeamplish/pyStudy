# str1 = "Itheima is a brand of Itcast"
# a_times = 0
# for i in str1:
#     if i == "a":
#         a_times += 1
# print(f"str1中有{a_times}个a")

"""
range(start, num, step)
函数返回的是一个可迭代对象 range(start, num)
start 从几开始,默认0
num 目标数字
step 每次循环间隔
"""
# num = 10
# for i in range(5, num, 4):
#     print(i)
# print(range(3))

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i}*{j}={i * j}", end="\t")
    if i == 6:
        continue
    elif i == 7:
        break
    print("")
