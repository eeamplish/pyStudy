def permission(temperature):
    """
    :param temperature: 体温
    :return: none
    :这里是注释
    """
    if temperature >= 37.5:
        print("发烧了")
    else:
        print("体温正常，请进")


temp = float(input("请输入你的体温"))
permission(temp)