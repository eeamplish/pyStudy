dict1 = {
    "力宏": {
        "部门": "科技部",
        "工资": 3000,
        "级别": 1
    },
    "杰伦": {
        "部门": "市场部",
        "工资": 5000,
        "级别": 2
    },
    "俊杰": {
        "部门": "市场部",
        "工资": 7000,
        "级别": 3
    },
    "学友": {
        "部门": "科技部",
        "工资": 4000,
        "级别": 1
    },
    "德华": {
        "部门": "市场部",
        "工资": 6000,
        "级别": 2
    },
}

for key in dict1:
    if dict1[key]["级别"] == 1:
        dict1[key]["工资"] += 1000
        dict1[key]["级别"] += 1

print(f"操作之后\n{dict1}")
