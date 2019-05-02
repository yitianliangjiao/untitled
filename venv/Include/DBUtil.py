import configparser
import pymysql

class DbBean:
    def __init__(self):
        print('初始化数据库连接')
        conf = configparser.ConfigParser()
        conf.read('resource/demo.conf')
        self.db_host = conf.get('mysqldb', 'db_host')
        self.db_port = conf.get('mysqldb', 'db_port')
        self.db_user = conf.get('mysqldb', 'db_user')
        self.db_pwd = conf.get('mysqldb', 'db_pwd')
        self.db_name = conf.get('mysqldb', 'db_name')

    def getsingle(self,sql):
        db = pymysql.connect(self.db_host, self.db_user, self.db_pwd, self.db_name)
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        print("getsingle result: %s " % data)
        cursor.close()
        db.close()
        return data
    def getList(self,sql):
        db = pymysql.connect(self.db_host, self.db_user, self.db_pwd, self.db_name)
        cursor = db.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        if not rows:
            return rows
        for r in rows:
            print(r)
        cursor.close()
        db.close()
        return rows
    def add(self,dbdict,tabname):
        if(type(dbdict).__name__!='dict'):
            raise Exception("应传入字典类"+type(dbdict).__name__)
        sql = "insert into "+tabname+" ("
        for key in dbdict.keys():
            sql += key+","
        sql = sql[:-1]
        sql += ") values ("
        for value in dbdict.values():
          sql += "'"+value + "',"
        sql = sql[:-1]
        sql += ")"
        db = pymysql.connect(self.db_host, self.db_user, self.db_pwd, self.db_name)
        cursor = db.cursor()
        print(sql)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()