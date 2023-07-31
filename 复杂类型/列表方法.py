# list1 = ["标点", [1, 2, 3], 4]
list1 = [1, 2, 3]
# str2_list = list()

# 列表方法

# 1. list.index(元素)
# 查询输入元素的索引值
# xxx = list1.index([1,2,3])

# 2. list.insert(下标, 元素)
# 指定下标里插入指定的元素
# list1.insert(1, "加入元素")

# 3. 追加元素
# list.append(元素)
# 列表最后加入元素

# list.extend(一批元素)
# 列表最后加入一批元素
# list1.append([4, 5, 6])  # [1, 2, 3, [4, 5, 6]]
# list1.extend([4, 5, 6])  # [1, 2, 3, 4, 5, 6]

# 4. 删除元素
# del list[下标]  # 单纯删除 无返回值
# del list1[1]

# list.pop(下标)  # 有返回值 返回值为删除的元素
# popEle = list1.pop(1)

# list.remove(元素)  # 删除列表第一个匹配的元素项
# list1.remove(1)

# list.clear()  # 清空列表

# list.count(元素)  # 统计列表中指定元素的个数 返回int型数字
# len(list)  # 统计列表中元素的个数 返回int型数字
# print(list1.count(1))
# print(len(list1))

print(list1)
