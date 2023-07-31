str1 = "脆脆熊"
str2 = "糯米锅巴"
num1 = 133
float1 = 13.14
# print(str1, str2)
# print(str1 + str2)
# pri_msg = "我是一个%s , 我爱吃%s" % (str1, str2)
# pri_msg = "我是一个%s , 我爱吃%s" % (str1, str2)
# 精度控制 %m.nd/s/f
# m 控制宽度 如果m小于实际宽度 则等同于没写
# n 控制小数点位数
# pri_msg = "%d包%s一共%6.2f元, %s爱吃" % (num1, str2, float1, str1)

# f"{}"
# print(f"每日增长系数：{growth_ratio:.1f}，经过{growth_days}天的增长，股价到达{cur_price*(growth_ratio**growth_days):.2f}")
pri_msg = f"{num1}包{str2}一共{float1}元, {str1}爱吃"

print(pri_msg)
