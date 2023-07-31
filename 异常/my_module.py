# 其他文件用 * 导入时只会导入 [] 里的方法
__all__ = ["test"]


def test(x, y):
    return x + y


def minus(x, y):
    return x / y


# 右键运行的时候会运行下面的代码
# 导入的时候不会运行
if __name__ == '__main__':
    test(1, 3)
