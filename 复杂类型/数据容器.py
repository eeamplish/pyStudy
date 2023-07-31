# 一.序列
# 内容连续、有序，可使用下标索引一类的数据容器
# 可以有重复元素
# 列表、元组、字符串等
# 二.非序列
# 不可使用下标索引一类的数据容器
# 不支持重复元素
# 集合(set)、字典(dict)

# 常用操作
# 1.切片：从一个序列中取出一个子序列
# 序列[开始下标:结束下标:步长]

# list1 = list(range(0, 6))
# list1_cut = list1[1:4:2]

# str1 = "012345"
# str1_cut = str1[1:4:2]

# tuple1 = tuple(range(0, 6))
# tuple1_cut = tuple1[1:4:2]
# tuple1_cut = tuple1[1:5:-1]  # 结果为()
# tuple1_cut = tuple1[::-1]  # 结果为(5, 4, 3, 2, 1, 0)

# print(tuple1)
# print(tuple1_cut)

str2 = "万过薪月，员序程马黑来，nohtyp学"
# 从字符串中得到黑马程序员
str2_res = str2[::-1].split("，")[1].strip("来")
print(str2_res)


