import random

num1 = random.randint(1, 100)  # [a,b]
times = 1
# num2 = random.randrange(1, 100)  # [a,b)
# num3 = random.uniform(1, 100)  # 生成随机浮点数
input_num = int(input("这里有一个1-100的整数，看你几次能猜对，猜猜看吧 "))
while input_num != num1:
    if input_num > num1:
        input_num = int(input("猜的太大了，再试试 "))
    elif input_num < num1:
        input_num = int(input("猜的太小了，再试试 "))
    times += 1
print(f"恭喜你猜对了，一共猜了{times}次")
