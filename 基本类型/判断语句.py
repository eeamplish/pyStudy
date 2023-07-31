# print(True == 1) True
# print(False == 0) True

# age = 8
# if age > 18:
#     print("成年人")
#
# print("巴拉巴拉吧")

# age = input("input your age ")
# if int(age) >= 18:
#     print("成年人游玩需要买票10元")
#     print("祝您游玩愉快")
# else:
#     print("未成年人禁止进入")

height = int(input("请输入您的身高 "))
if height >= 140:
    print("请买票进入")
elif height >= 100:
    print("请买半票进入")
else:
    print("小个子不用买票，直接进去吧")
print("祝您玩的开心~")
