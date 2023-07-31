# 设计类
class Student:
    name = None
    gender = None
    nation = None
    native_place = None
    age = None

    def say_hi(self):
        print(f"大家好，我是{self.name}，今年{self.age}，来自{self.nation}{self.native_place}")

    def say_hi2(self, lrc):
        print(f"我是{self.name}，{lrc}")


# 创建对象
stu_1 = Student()

# 对象属性赋值
stu_1.name = "xiaoA"
stu_1.gender = "男"
stu_1.nation = "china"
stu_1.native_place = "hubei"
stu_1.age = 11

stu_1.say_hi()
stu_1.say_hi2("所有人都得死")
