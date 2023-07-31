# json.dumps()
# 将Python数据结构转换为JSON,即dict类型转成str类型

# json.dump()
# 用于将dict类型的数据转成str类型&#xff0c;并写入到json文件。

# json.loads()
# 将JSON编码的字符串转换回Python数据结构;即str类型转换成dict类型

# json.load()
# 用于从json文件中读取数据

import json
data = [
    {"name": "小小A", "age": 14, "gender": True},
    {"name": "小B", "age": 26, "gender": True},
    {"name": "小CC", "age": 77, "gender": False}
]

# ensure_ascii 参数表示 输出是否ascii码，传布尔类型
dum_data = json.dumps(data, ensure_ascii=False)

data_str = '[{"name": "小小A", "age": 14, "gender": true}, {"name": "小CC", "age": 77, "gender": false}]'

loads_data = json.loads(data_str)
print(loads_data, type(loads_data))
