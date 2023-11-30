from pymysql import Connection

# 与数据库建立连接
dbdata = Connection(
    host="localhost",  # 主机名 ip
    port=3306,  # 端口号
    user="root",  # 账号
    password="123456",  # 密码
    autocommit=True  # 如果设置为true 修改数据时不需要调用commit方法也能操作数据库数据
)
# 获取服务器版本号
# print(dbdata.get_server_info())

# 获取游标对象
cursor = dbdata.cursor()

# 选择数据库
dbdata.select_db("test11")

# 对数据库执行操作，括号里用数据库操作语法写
# execute  返回int数据
# cursor.execute("create table test_py(id int, gameName varchar(10))")
cursor.execute("select * from singer where id > 5")
# cursor.execute("insert into singer(id, name, gender, song) VALUES (1, '周杰伦', '男', '雨下一整晚')")
# cursor.execute("delete from singer where id = 1")


# cursor.fetchall 里的数据是上面 execute 方法查询到的数据
xxx: tuple = cursor.fetchall()
print(xxx)

# 如果有对数据库进行数据更改，需要调用 commit 方法
# dbdata.commit()

# 关闭连接
dbdata.close()
