file = open("写.txt", "r", encoding="utf-8")
write_file = open("bill.txt.bak", "a", encoding="utf-8")
for line in file:
    if line.find("测试") != -1:
        continue
    write_file.write(line)
file.close()

# 调用close会自动调用flush 不用专门调用flush
write_file.close()

