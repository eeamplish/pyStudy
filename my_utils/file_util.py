def print_file_info(file_name):
    """
    :param file_name: 文件路径
    : 打印文件内容
    """
    try:
        file = open(file_name, "r", encoding="utf-8")
        print(file.read())
    except Exception as e:
        print(e)
    else:
        file.close()


def append_to_file(file_name, data):
    """
    :param file_name: 文件路径
    :param data: 追加写入到文件的内容
    """
    file = open(file_name, "a", encoding="utf-8")
    file.write(data)
    file.close()
