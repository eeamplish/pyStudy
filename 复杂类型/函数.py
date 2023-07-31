str1 = "书覅撒旦法撒旦法收到"
str2 = "12345678910"


# str_length = len(str1)
# print(str_length)


def str_length_calc(string):
    count = 0
    for i in string:
        count += 1
    print("str1的长度是", count)


def add(x, y):
    return x + y


# print(f"3+4的值是{add(3, 4)}")


# 函数可以有多个返回值且多个返回值类型不用相同
def return_test():
    a = 12
    b = [1, 2, 3]
    c = {
        "name": "C",
        "age": 12
    }
    return a, b, c


# x, y, z = return_test()
# print(x)
# print(y)
# print(z)


def user_info(name, age, hobby):
    print(f"我叫{name}，今年{age}岁，爱好是{hobby}")


# user_info(666, hobby="跑步", age="xxx")
# 关键字参数
# 位置参数必须在关键字参数的前面，否则会报错


def not_confirm_len(*args):
    # *args 位置不定长函数
    # *args 作为元组存在
    # *args 直接传值
    print(args)
    print(type(args))  # <class 'tuple'>


def not_confirm_len2(**kwargs):
    # **kwargs 关键字不定长
    # **kwargs 作为字典存在
    # **kwargs 传键值对
    print(kwargs)
    print(type(kwargs))  # <class 'dict'>


not_confirm_len("666", 666, "jacket")
not_confirm_len2(name="xiaoc", age=666, like="jacket")

