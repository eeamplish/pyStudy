class Phone:
    name = None
    price = None

    def __init__(self, name, price):
        self.name = name
        self.price = price

    # 私有变量
    __privation_num = 6

    # 私有方法
    def __netting(self):
        print(f"{self.name}: {self.price}元")

    def custom(self):
        if self.__privation_num > 5:
            self.__netting()
        else:
            print("通用方法")


p1 = Phone("安卓", 666)

p1.custom()

# 私有变量 私有方法 不能被创建的对象直接使用
# 下面两个调用都会报错
# print(p1.__privation_num)
# print(p1.__netting())


