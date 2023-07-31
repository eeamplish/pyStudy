# 写入步骤

# 1、打开文件
# open(name, mode, encoding)
# mode参数 r、w、a、x，分别代表读、写、追加、创建新文件
# w 写会清空原文件

# 2、写入文件 (写入的文件存在缓存区 不刷新不会写入到文件里)
# file.write()

# 3、刷新文件
# file.flush()

# file = open("写.txt", "w", encoding="utf-8")
# file.write("```\n")
# file.write("我是你爹\n你是谁")
# file.write("我是你爹\n你是谁\n")
# file.write("```")
# file.flush()

# file = open("新建.md", "x", encoding="utf-8")
# file.write("## なんだこれ\n")
# file.write("　这是个啥　\n")


file = open("新建.md", "a", encoding="utf-8")
file.write("新加的看看")
file.flush()
file.close()

