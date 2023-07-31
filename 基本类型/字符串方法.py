# 1. 查找索引 str.index(xxx)
# xxx 在 str 中第一个元素的下标

# 2. 字符串替换 str.replace("字符串1", "字符串2")
# 字符串2 替换 字符串1
# 返回一个新的字符串

# 3. 字符串分割 str.split()
# 括号里不能是空字符串 但是可以是带空格的字符串
# str1.split(" ") 可以
# str1.split("") 不可以
# 按照指定分隔符分割字符串 返回 list 对象

# 4. 去除前后空格 str.strip(传参)
# 不传参时是去空格，传参是去指定字符串
# "12acada pxo piouid21 ".strip("12a")  结果是 "cada pxo piouid21"
# 去除是按单个传参算的 "12a" 是去除前后 "1" "2" "a"

# 5. 统计字符在字符串中出现的次数 str.count()

# str1 = "12acada pxo piouid21 "
# res = str1.count("a")
# print(res)

str2 = "itheima itcast boxuegu"
it_count = str2.count("it")
print(f"字符串中it数是{it_count}")
str3 = str2.replace(" ", "|") # 返回个新的字符串
print(f"空格替换|之后字符串是{str3}")
after_split = str3.split("|")
print(f"按|切割之后的列表是{after_split}")

