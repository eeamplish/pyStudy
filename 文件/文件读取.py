file = open("lrc_test.txt", "r", encoding="utf-8")
# print(file.read())
# showTimes = 0
# for line in file:
#     # print(line)
#     if line.find("の") != -1:
#         showTimes += 1
#         print(line)

# for line in file:
#     temp_count = line.count("く")
#     showTimes += temp_count
showTimes = file.read().count("く")
print(f"く 共出现了{showTimes}次")
# str1 = "abcdef"
# print(str1.find("bcd"))

