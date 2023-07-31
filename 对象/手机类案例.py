class Phone:
    __is_5g_enable = 0

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5G开启")
        else:
            print("5G关闭，使用4G网络")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

    def father_method(self):
        print(f"爹的方法{self}")


# p1 = Phone()
# p1.call_by_5g()


