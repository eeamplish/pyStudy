import copy
import random


# room_id = "111"
# file = open(f"{room_id}_danmu.txt", "a", encoding='utf-8')
# file.write("xxxxx\n")
# file.close()

# 2/3 * 1/2 = 1/3
# 1/3 5打砰砰
# 2/3 * 1/2


# 是否能全解
def start_calc(hp_list, damage):
    copy_list = copy.deepcopy(hp_list)
    for i in range(damage, 0, -1):
        if len(copy_list) == 0:
            break
        random_index = random.randint(0, len(copy_list) - 1)
        if copy_list[random_index] - i <= 0:
            del copy_list[random_index]
        else:
            copy_list[random_index] -= i

    return len(copy_list) == 0


# 全解概率
def solve_rate(hp_list, damage):
    success_time = 0
    gg_time = 0
    for j in range(0, 10000):
        if start_calc(hp_list, damage):
            success_time += 1
        else:
            gg_time += 1

    return {
        "success_time": success_time,
        "gg_time": gg_time
    }


# 打星之后 list 血量
def after_start_list(hp_list, damage):
    copy_list = copy.deepcopy(hp_list)
    for i in range(damage, 0, -1):
        if len(copy_list) == 0:
            break
        random_index = random.randint(0, len(copy_list) - 1)
        if copy_list[random_index] - i <= 0:
            del copy_list[random_index]
        else:
            copy_list[random_index] -= i
    return copy_list


# 打星之后 list 血量
# 显示各位置的血量
def after_start_list2(hp_list, damage):
    copy_list = copy.deepcopy(hp_list)
    index_list = list(range(0, len(copy_list)))
    for i in range(damage, 0, -1):
        if len(index_list) == 0:
            break
        random_index = index_list[random.randint(0, len(index_list) - 1)]
        if copy_list[random_index] - i <= 0:
            copy_list[random_index] = 0
            index_list.remove(random_index)
        else:
            copy_list[random_index] -= i
    return copy_list


# list 血量分布
def hp_distribution(hp_list, damage):
    temp_dict = {}
    for j in range(0, 10000):
        ato_list = after_start_list2(hp_list, damage)
        if str(ato_list) in temp_dict.keys():
            temp_dict[str(ato_list)] += 1
        else:
            temp_dict[str(ato_list)] = 1

    return temp_dict


param_list = [5, 3, 4]
param_damage = 5
print(hp_distribution(param_list, param_damage))
print(solve_rate(param_list, param_damage))

