from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
import copy

listA = zip(Faker.provinces, Faker.values())
listB = zip(Faker.provinces, Faker.values())

# 中国地图
# c = (
#     Map()
#     .add("商家A", [list(z) for z in listA], "china")
#     .add("商家B", [list(z) for z in listB], "china")
#     # add 多个参数的话则是按市名相加
#     # [['广东省', 79], ['北京市', 91], ['上海市', 142], ['江西省', 45], ['湖南省', 128], ['浙江省', 45], ['江苏省', 42]] <class 'list'>
#     # [['广东省', 96], ['北京市', 67], ['上海市', 143], ['江西省', 41], ['湖南省', 44], ['浙江省', 82], ['江苏省', 60]] <class 'list'>
#     .set_global_opts(title_opts=opts.TitleOpts(title="Map-基本示例"))
#     .render("map_base.html")
# )


# 广东地图
c = (
    Map()
    .add("商家A", [list(z) for z in zip(Faker.guangdong_city, Faker.values())], "广东")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-广东地图"), visualmap_opts=opts.VisualMapOpts()
    )
    .render("map_guangdong.html")
)

