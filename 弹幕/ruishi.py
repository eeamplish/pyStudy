import copy
import random


def fighting(arr):
    win_arr = []
    lose_arr = []
    while len(arr) > 0:
        random_index = random.randint(1, len(arr) - 1)
        win_arr.append(arr[0] if arr[0] < arr[random_index] else arr[random_index])
        lose_arr.append(arr[0] if arr[0] > arr[random_index] else arr[random_index])
        arr.pop(random_index)
        arr.pop(0)

    return {
        "win": win_arr,
        "lose": lose_arr
    }


# times 几胜晋级or几败淘汰
# team_num 队伍数量 2^n
def get_promotion_team(times, team_num):
    team_obj = {}  # 每个队最后的战绩汇总
    all_obj = {}  # 全部战绩
    # i代表场次 j代表胜场
    for i in range(0, 2 * times):
        if i == 0:
            team_obj["0-0"] = list(range(1, team_num + 1))
            all_obj["0-0"] = list(range(1, team_num + 1))
        for j in range(0, i + 1):
            if j >= times or i - j >= times:
                continue
            cur_record = f"{j}-{i - j}"
            fight_obj = fighting(team_obj[cur_record])
            fill_all_obj = copy.deepcopy(fight_obj)
            # 赢的队战绩
            win_record = f"{j + 1}-{i - j}"
            if team_obj.get(win_record) is not None:
                team_obj[win_record] += fight_obj["win"]
            else:
                team_obj[win_record] = fight_obj["win"]
            # 输的队战绩
            lose_record = f"{j}-{i - j + 1}"
            if team_obj.get(lose_record) is not None:
                team_obj[lose_record] += fight_obj["lose"]
            else:
                team_obj[lose_record] = fight_obj["lose"]

            if all_obj.get(lose_record) is not None:
                all_obj[lose_record] += fill_all_obj["lose"]
            else:
                all_obj[lose_record] = fill_all_obj["lose"]
            if all_obj.get(win_record) is not None:
                all_obj[win_record] += fill_all_obj["win"]
            else:
                all_obj[win_record] = fill_all_obj["win"]

    # print(team_obj.keys())
    # for key in list(team_obj.keys()):
    #     if not team_obj[key]:
    #         team_obj.pop(key)
    # del team_obj[key]

    jj_team = []
    xx_team = []
    for key in list(team_obj.keys()):
        if f"{times}-" in key:
            jj_team += team_obj[key]
        else:
            xx_team += team_obj[key]

    # print(jj_team)
    # print(xx_team)
    return {
        "final": team_obj,
        "jj_team": jj_team,
        "xx_team": xx_team,
        "all": all_obj
    }


times_obj = {}
# print(get_promotion_team(3, 16)["all"])
for m in range(16):
    times_obj[m + 1] = 0
for i in range(0, 10000):
    jj = get_promotion_team(3, 16)["jj_team"]
    for key in jj:
        times_obj[key] += 1
print(times_obj)
