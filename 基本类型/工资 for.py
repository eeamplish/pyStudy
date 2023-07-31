import random
total_sala = 10000
for i in range(21):
    num1 = random.randint(1, 10)  # [a,b]
    if num1 <= 5:
        print(f"员工{i}，绩效分{num1}，低于5，不发工资，下一位")
        continue
    total_sala -= 1000
    print(f"向员工{i}发放工资1000元，账户余额还剩余{total_sala}元")
    if total_sala == 0:
        print("工资发完了，下个月领取吧")
        break

