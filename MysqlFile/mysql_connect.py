# import mysql.connector
import pymysql
from DataHandle.data_collection import DataCollection


class MysqlConnect(DataCollection):
    def __int__(self):
        super(MysqlConnect, self).__int__()
        self.parameter = 50
        self.db_host = "123.56.95.138"  # 属性应私有
        self.db_port = 3306  # 注意，端口是int类型，不能有引号，否则会报错
        self.db_user = 'root'
        self.db_password = 'root'
        self.db_database = 'power'  # 数据库名
        self.db_charset = 'utf-8'
        self.db = pymysql.connect(
            host=self.db_host,
            port=self.db_port,
            user=self.db_user,
            passwd=self.db_password,
            database=self.db_database,
            charset=self.db_charset
        )

    # def isConnection(self):


    def insert(self):
        # users_values = self.custom_data()
        users_values = [(1, -10.292204, -0.028390809198884894), (2, -10.037611, -0.003747007131477805)]
        print(users_values)
        coon = pymysql.connect(user='root', passwd='root', db="power", port=3306, host='123.56.95.138', charset='utf8')
        # for num in range(1, 50000):
        #     usersvalues.append((users_values))  # 注意要用两个括号扩起来
        # conn = connect(host='主机名', port='端口号', user='用户名', password='密码', database='数据库名', charset='utf8')
        # sql = """INSERT INTO MHZ-10 (own_data,Agl_4418B,error_data) VALUES (%s,%s,%s);"""
        # sql = 'insert into MHZ-10(own_data,Agl_4418B,error_data) values(%s,%s,%s)'
        # sql = '''INSERT INTO MHZ-10(own_data,Agl_4418B,error_data) VALUES (%s,%s,%s)'''
        sql = """INSERT INTO MHZ-10 (own_data,Agl_4418B,error_data) VALUES (1, -10.292204, -0.028390809198884894);"""
        cs = coon.cursor()  # 获取光标
        cs.execute(sql)
        # 注意这里使用的是executemany而不是execute，下边有对executemany的详细说明
        # cs.executemany(sql, users_values)
        coon.commit()
        cs.close()
        coon.close()
        print('OK')


    def delete(self):
        pass

    def query(self):
        pass

    def create_table(self,name):
        pass

    def excute_cont(self):
        """执行命令的次数"""
        count = 0
        while count <= self.parameter:
            count = count + 1
if __name__ == '__main__':
    m = MysqlConnect()
    print(m.insert())