def add(x, y, z):
    temp = z(x, y)
    return temp + y


def minus(x, y):
    return x - y


# print(add(1, 2, minus))

# lambda 传入参数: 函数体(只能一行代码)
print(add(1, 2, lambda x, y: x - y))
