
def copy_file(name1, name2):
    """
    :param name1: 被复制的文件名
    :param name2: 复制之后的文件名
    :return: 无
    """
    file = open(name1, "r", encoding="utf-8")
    file2 = open(name2, "a", encoding="utf-8")
    file2.write(file.read())
    file.close()
    file2.close()
