# list1 = [21, 25, 21, 23, 22, 20]
# list1.append(31)
# print(list1)
# list1.extend([29, 33, 30])
# print(list1)
# afterPop1 = list1.pop(0)
# print(list1, afterPop1)
# afterPop2 = list1.pop(len(list1)-1)
# print(list1, afterPop2)
# Index31 = list1.index(31)
# print(Index31)
# print(list1)


# i = 0
# while i < len(list1):
#     print(i, list1[i])
#     i += 1

# for ele in list1:
#     print(ele, list1.index(ele))

list2 = range(1, 11)
# list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []
# while
# i = 0
# while i < len(list2):
#     if list2[i] % 2 == 0:
#         even_list.append(list2[i])
#     i += 1

# for
for i in list2:
    if i % 2 == 0:
        even_list.append(i)
print(even_list)
