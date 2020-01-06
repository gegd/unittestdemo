import sys
import os
sys.path.append(os.getcwd())
from data.get_data import GetData
from common.send_request import RequestAction
from util.compare_str import is_equal
from common.run_depend import DependData
from util.send_email import SendEmail
from util.operation_cookie import OperationCookie
from util.operation_json import OperationJson
import requests
import json

class RunTest():
    def __init__(self):
        self.data = GetData()
        self.run_method = RequestAction()
        self.sen = SendEmail()
    def run_test(self):
        pass_count = []
        fail_count = []
        row_counts = self.data.get_nrows()
        for i in range(0,row_counts):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_url(i)
                request_method = self.data.get_request_method(i)
                request_data = self.data.get_request_data(i)
                header = self.data.get_header(i)
                expect = self.data.get_expect_by_case(i)
                depend_key = self.data.get_depend_key(i)
                print(header)
                if depend_key != '':
                    depend_model = DependData(depend_key)
                    depend_data = depend_model.get_depend_data(i)
                    depend_data_id = self.data.get_field_data_id(i)
                    request_data[depend_data_id] = depend_data
                    print(request_data)

                if header == 'write':
                    res = requests.post(url,request_data)
                    oper_cookie = OperationCookie(res)
                    oper_cookie.write_cookie() 
                    res = json.dumps(res.json(),ensure_ascii=False)
                    
                elif header == 'read':
                    oper_json = OperationJson()
                    cookie_json = oper_json.read_cookie_json()
                    res = self.run_method.run_main(url,request_method,request_data,cookie_json)
                else:
                    res = self.run_method.run_main(url,request_method,request_data)
                
                if is_equal(expect,res):
                    self.data.write_res(i,"pass")
                    pass_count.append(i)
                else:
                    self.data.write_res(i,res)
                    fail_count.append(i)
        self.sen.send_main(pass_count,fail_count)
if __name__ == "__main__":
    run_all = RunTest()
    run_all.run_test()