from pyspark import SparkConf, SparkContext

# 使用pySpark完成数据处理 需要先构建一个环境入口对象

# 创建sparkConf类对象
conf = SparkConf().setMaster("local[2]").setAppName("test_spark_app")

# 基于sparkConf类对象创建sparkContext类对象
sc = SparkContext(conf=conf)

#
print("ver", sc.version)
print("sc", sc)

# for key in sc:
#     print(key, sc[key])

# 停止sc对象的运行
sc.stop()


