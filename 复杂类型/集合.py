# 定义集合
# set 内元素不能重复
set1 = {"a", "b", "c"}
set2 = set("bdf")

# 集合方法
# 1.添加元素
# set.add(元素)
# 2.移除元素
# set.remove(元素)
# 3.随机取出一个元素
# set.pop() 返回值为取出的元素，取出后set里的值会清除#
# 4.清空集合
# set.clear() 返回值为取出的元素，取出后set里的值会清除

# 5.取出集合的差集（集合1有 集合2没有的）
# 集合1.difference(集合2)
# 原集合不变，返回一个新的集合
# 6.消除集合的差集（删除集合1中 集合2有的元素）
# 集合1.difference_update(集合2)
# 集合1修改，集合2不变
# 6.集合合并
# 集合1.union(集合2)
# 原集合不变，返回一个新的集合

# set1.add("d")
# set1.add("c")
# set1.remove("b")
# set_pop = set1.pop()
# set1.clear()
# set3 = set1.difference(set2)
# set3 = set1.difference_update(set2)
# set3 = set1.union(set2)
# print(set1)
# print(set2)

list1 = ["黑马程序员", "传智播客", "黑马程序员", "传智播客", "itheima", "itcast", "itheima", "itcast", "best"]

set3 = set()
for i in list1:
    set3.add(i)
print("去重后", set3)

