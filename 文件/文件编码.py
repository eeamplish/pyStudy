# py操作文件
# 1、打开文件
# 2、读写文件
# 3、关闭文件
import time

# 1.打开
# open(name, mode, encoding)
# name 打开的目标文件名字符串（可以包含具体路径）
# mode 设置打开的模式：只读，写入，追加等。默认为只读(r)
# encoding 编码格式（一般是utf-8）

# with open(name, mode, encoding) as file:
# 这种方式操作完文件之后会自动调用close方法

# file = open("C:/Users/wzm/Desktop/newform.txt", "r", encoding="UTF-8")
# file = open("C:/Users/wzm/Desktop/票据日期限制.md", "r", encoding="UTF-8")
file = open("111.txt", "r", encoding="UTF-8")

# 2.读取文件 read(int)
# int 表示读写的长度
# 一个文件多次调用 read 的时候 会从上一次文件调用结尾的地方开始
# print(file.read(10))
# print(file.read())

# readline() 读取文件的第一行
# print(file.readline())

# readlines() 读取文件的全部行
# 返回<class 'list'> ['这是一个寂寞的天\n', '吓着有写伤心的域\n', '不用等天晴']
# print(file.readlines())

for i in file:
    print(i)

# 3.关闭文件
# close()
# 不调用close 时在外面直接点击文件打开会报已经被占用(win11没有这个问题？)

# time.sleep(100000)
# file.close()


