# 元组 只可读不可改
# (元素1, 元素2, ...)
# 括号创建元组时 只有一个元素的话结尾需要加逗号 否则是字符串
# (元素1,)
# tuple(data)  # data 表示可以转化为元组的数据，包括字符串、元组、range 对象等。

# tup1 = ("xxx", 3, [1, 2])
# tup2 = tuple("qwe")
# print(tup2)

tup3 = ("走杰伦", 11, ["football", "music"])
ageIndex = tup3.index(11)
print(ageIndex, "年龄下标")
print(tup3[0], "姓名")
del tup3[2][0]
print(tup3, "删除爱好的足球")
tup3[2].append("coding")
print(tup3, "爱好增加coding")

