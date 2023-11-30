# 完成某个行为时 使用不同的对象会得到不同的状态


class Animal:
    # Animal 可以视为一个抽象类
    # 抽象类多用于顶层设计（设计标准），以便子类做具体实现
    # speak 是抽象方法 子类必须复写父类的抽象方法
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def make_noisy(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()

make_noisy(dog)
make_noisy(cat)

