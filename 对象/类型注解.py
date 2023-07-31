import random
from typing import Union

num1: int = 667


def xxx(a: int, b: str) -> list:
    print(f"{a}, {b}")
    return [555, 777]


# print(random.randint(6, 8))
# return_list = xxx(3, "5")
# print(return_list)

# 如果数据中有多种类型 可以使用Union
mix_list: list[Union[int]] = [111, "frd", 90]
print(mix_list)


def union_func(a: Union[str, int], b: Union[list, dict]) -> dict:
    b[0] = a
    return b


# aa = union_func(666, ["787", 9527])
aa = union_func(666, {"0": "sdfs"})
print(aa)
