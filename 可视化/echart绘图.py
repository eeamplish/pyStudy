import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker

# 折线图示例
# c = (
#     Line()
#     .add_xaxis(Faker.choose())
#  x轴数据 ['哈士奇', '萨摩耶', '泰迪', '金毛', '牧羊犬', '吉娃娃', '柯基'] <class 'list'>
#     .add_yaxis("商家A", Faker.values())
#     .add_yaxis("商家B", Faker.values())
#  y轴数据 [30, 97, 28, 26, 100, 124, 140] <class 'list'>
#     .set_global_opts(title_opts=opts.TitleOpts(title="Line-基本示例"))
#  全局配置项
#     .render("line_base.html")
# )


line = Line()
line.add_xaxis(['哈士奇', '萨摩耶', '泰迪'])
line.add_yaxis("A店价格", [3, 8, 33])
line.add_yaxis("B店价格", [15, 4, 66])
line.render()

