def str_reverse(s):
    """
    :param s: 输入字符串
    :return: 返回翻转的字符串
    """
    # 方法1
    # list1 = list(reversed(list(s)))
    # str2 = "".join(list1)
    # return str2

    # 方法2
    # str_rer = "".join(s.sorted(reversed=True))
    # return str_rer

    # 方法3 切片
    str_rer = s[::-1]
    return str_rer


def substr(s, x, y):
    """
    :param s: 传入字符串
    :param x: 截取下标起始位置
    :param y: 截取下标结束位置
    :return: 截取字符串
    """
    str_slice = s[x:y]
    return str_slice


if __name__ == '__main__':
    print(str_reverse("1234"))
    print(substr("12345", 1, 4))
