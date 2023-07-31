class Hero:
    name = None
    position = None
    lrc = None
    difficulty = None

    def __init__(self, name, position, lrc, difficulty):
        self.name = name
        self.position = position
        self.lrc = lrc
        self.difficulty = difficulty

    def self_intro(self):
        if self.difficulty > 5:
            print(f"{self.lrc}；我是{self.name}，定位{self.position}，不推荐新手玩")
        else:
            print(f"{self.lrc}；我是{self.name}，定位{self.position}，新人必玩")


# hero1 = Hero("狗头", "上单", "生与死轮回不止，我们生他们死", 5)
# hero2 = Hero("发条", "中单", "我们会帮你杀敌，这肯定很有趣", 10)
# hero1.self_intro()
# hero2.self_intro()

for i in range(10):
    here_name = input("请输入英雄名字：")
    here_position = input("请输入英雄定位：")
    here_diff = int(input("请输入英雄难度："))
    here_lrc = input("请输入英雄台词：")
    hero_new = Hero(here_name, here_position, here_lrc, here_diff)
    print(f"{i+1} 号英雄信息录入完成！")
    hero_new.self_intro()

