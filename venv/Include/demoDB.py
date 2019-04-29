import pymysql
db_host = localhost
db_port = 3306
db_user = root
db_pwd  = 123456
db_name = test

db = pymysql.connect("localhost","root","123456","test" )
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print ("Database version : %s " % data)
db.close()