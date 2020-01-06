import pymysql
import json

class OperationDB():
    def __init__(self,case_name):
        self.sql = self.get_sql(case_name)
        self.conn = pymysql.connect(host='106.14.126.145',user='root',passwd='root',db='my_auto_test',port=3306,charset='utf8')
        self.cur = self.conn.cursor()

    def search_one(self):
        self.cur.execute(self.sql)
        result = self.cur.fetchall()
        # result = json.dumps(result)
        return result[0][2]

    def get_sql(self,case_name):
        expect = "select * from get_expect where case_name = %s%s%s" %("'",case_name,"'")
        print(expect)
        return expect


if __name__ == "__main__":
    oper_db = OperationDB('login_001')
    result = oper_db.search_one()
    print(result[0][2])

