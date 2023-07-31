# 1.len()
# 2.max()
# 3.min()
# 4.sorted("", reverse=True)  #第二个参数可选 传就是逆序
# 排序时容器内只能是同类型元素

list1 = [1, 2, 3, 6, 8, 4]
list2 = ["b", "c", "a", "d", "o", "p"]
list_sort = sorted(list1, reverse=True)
list2_sort = sorted(list2, reverse=True)
# print(list1)
# print(list_sort)
# print(list2)
# print(list2_sort)

print(max(list1))
print(min(list1))
print("a" > "A")
