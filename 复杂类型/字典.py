# {} 相当于js对象
# dict()
# 存储键值对
# dic1 = dict()
# dic1["a"] = 666
dict2 = {
    "name": "hurry",
    "age": 13,
    "hobby": "singing"
}

# 删除元素
# dict.pop(key) 返回值为key对应的值
# dic_pop = dict2.pop("age")

# 清空元素
# dict.clear()
# dict2.clear()


dict2_keys = dict2.keys()
# print(dict2_keys, type(dict2_keys)) 打印结果如下
# dict_keys(['name', 'age', 'hobby']) <class 'dict_keys'>
# dict2_keys[1] dict_keys不支持下标取元素，这种写法会报错

for key in dict2:
    print(key, dict2[key])
# print(dict2_keys, type(dict2_keys))

