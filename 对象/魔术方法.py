
# python 类内置方法可以叫魔术方法

# 1. __init__ 构造方法
# 2. __str__ 字符串方法
# 3. __lt__ 小于
# 4. __le__ 小于等于
# 5. __eq__ 符号比较

class Student:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"{self.name}, {self.age}")

    def __lt__(self, other):
        # other 是大于号左边 小于号右边的参数
        print("other1", other.name)
        return self.age < other.age

    def __eq__(self, other):
        # other 是大于号左边 小于号右边的参数
        print("other2", other.name)
        return self.age > other.age


stu1 = Student("A", 18)
stu2 = Student("B", 29)

# 这里大于调用 __lt__ 方法
print(stu1 == stu2)
