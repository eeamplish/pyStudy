from data import userdata
from pymysql import Connection


# 与数据库建立连接
conDB = Connection(
    host="localhost",  # 主机名 ip
    port=3306,  # 端口号
    user="root",  # 账号
    password="123456",  # 密码
    autocommit=True  # 如果设置为true 修改数据时不需要调用commit方法也能操作数据库数据
)

# 获取游标对象 选择数据库
cursor = conDB.cursor()
conDB.select_db("test11")

# 执行数据库语言 创建表
# cursor.execute("create table shareCenter (id varchar(30), originalCurrency varchar(50), comments varchar(50), companyCode varchar(50), profitCenter varchar(50), dataSource varchar(10), trsdat varchar(50), acceptCurrency varchar(20))")


# 插入数据库的数据
# "fsscId": "1010000025102967"
# "originalCurrency": "30.00",
# "comments": "其他费用其他费用",
# "companyCode": "TCL王牌电器（惠州）有限公司(1503)",
# "profitCenter": "GOC全球运营中心(1503M19000)",
# "dataSource": "09",
# "trsdat": "2023-08-29",
# "acceptCurrency": "人民币(CNY)",

insStr = ""
for item in userdata:
    # 一起插入的数据
    insStr += ("," if insStr else "") + f"('{item['fsscId']}', '{item['originalCurrency']}', '{item['comments']}', '{item['companyCode']}', '{item['profitCenter']}', '{item['dataSource']}', '{item['trsdat']}', '{item['acceptCurrency']}')"

    # 一条一条插入
    # insStr = f"('{item['fsscId']}', '{item['originalCurrency']}', '{item['comments']}', '{item['companyCode']}', '{item['profitCenter']}', '{item['dataSource']}', '{item['trsdat']}', '{item['acceptCurrency']}')"
    # print(insStr, "\n")
    # cursor.execute(f"insert into shareCenter (id, originalCurrency, comments, companyCode, profitCenter, dataSource, trsdat, acceptCurrency) VALUES {insStr}")

# 一起插入数据库
cursor.execute(f"insert into shareCenter (id, originalCurrency, comments, companyCode, profitCenter, dataSource, trsdat, acceptCurrency) VALUES {insStr} ")

# 关闭连接
conDB.close()


