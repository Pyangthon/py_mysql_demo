import MySQLdb

# 打开数据库
db = conn=MySQLdb.connect(host='localhost',port=3306,user='root',passwd='123456',db='test',charset='utf8')

# 使用cursor()方法操作游标
cursor = db.cursor

# 使用execute方法执行sql语句
cursor.execute("select version()")

# 使用fetchone()方法获取一条数据
data = cursor.fetchone()

print ("Database version : %s" % data)

# 关闭数据库连接
db.close()