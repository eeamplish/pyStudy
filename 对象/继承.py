import 手机类案例 as Imp


# 继承语法
# 单继承
# class xxx(父类):
# 多继承
# class xxx(父类1, 父类1, ... , 父类n):
class Phone2022(Imp.Phone):
    face_id = "10001"

    def call_by_5g(self):
        print("2022新功能，5g通话")


# p2 = Phone2022()
# p2.call_by_5g()
# p2.father_method()


class Biubiu:
    def biubiubiu(self):
        print("biubiubiu")

    def sing(self):
        print("Biubiu里的singing")


class Sing:
    def sing(self):
        print("singing")


# 继承时如果不需要写单独的方法或者变量可以使用pass跳过
# class Mp3(Biubiu, Sing):
#     pass

# 父类的方法可以用同名函数复写
class Mp3(Sing, Biubiu):
    def sing(self):
        print("dancing")
        # 如果父类有重名方法 super调用的是前面一个父类的方法
        # 这里sing调用的是Sing父类的方法
        super().sing()


m1 = Mp3()
m1.sing()
# m1.biubiubiu()
# Sing.sing(m1)

# 调用父类的成员或方法
# 成员
# 父类名.成员变量
# super().成员变量  # 只能在子类成员方法里用？

# 方法
# 父类名.成员方法(self)
# super().成员方法()  # 只能在子类成员方法里用？

