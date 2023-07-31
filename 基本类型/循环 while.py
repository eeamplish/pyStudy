# 求前n项和
# n = 100
# sum = 0
# x = 0
# while x <= n:
#     sum += x
#     x += 1
# print(f"从1开始前{n}项和是{sum}")

# 九九乘法表
# i = 1
# while i <= 9:
#     j = 1
#     cur_expression = ""
#     while j <= i:
#         cur_expression += f"{j}*{i}={i*j} "
#         j += 1
#     print(cur_expression)
#     i += 1
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={i*j}", end="\t")
        j += 1
    i += 1
    # print空内容等于换行
    print()
