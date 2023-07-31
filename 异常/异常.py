# 捕获异常：对bug进行提醒，整个程序继续运行
# 如果不捕获程序会停止运行

# 语法
# try:
# except:  # 捕获所有异常
# except NameError as e:  # 捕获指定异常

# try:
#     open("xxx.txt", "r", encoding="utf-8")
# except:
#     print("捕获异常")
# print("naninani")


try:
    # print(xxx)
    # print(1/0)
    print(111)
# 捕获多种异常
# e 为try里第一条报错的异常类型
# except (ZeroDivisionError, NameError) as e:

# 捕获全部异常
# e 为try里第一条报错的异常类型
except Exception as e:
    print(e)
else:
    print("没有异常")
finally:
    print("无论有无异常都要执行finally")
