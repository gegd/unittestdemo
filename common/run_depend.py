import os
import sys
sys.path.append(os.getcwd())
from data.get_data import GetData
from common.send_request import RequestAction
from jsonpath_rw import jsonpath,parse
import json

class DependData():
    def __init__(self,case_id):
        self.case_id = case_id
        self.data = GetData()
        self.reqAction = RequestAction()

    
    def run_depend(self):
        row_num = self.data.get_depend_line(self.case_id)
        depend_url = self.data.get_url(row_num)
        depend_method = self.data.get_request_method(row_num)
        depend_data = self.data.get_request_data(row_num)
        res = self.reqAction.run_main(depend_url,depend_method,depend_data)
        return json.loads(res)

    def get_depend_data(self,row):
        depend_key = self.data.get_field_key(row)
        response_data = self.run_depend()
        print(response_data)
        java_exe = parse(depend_key)
        madle = java_exe.find(response_data)
        return [match.value for match in madle][0]

        
        

if __name__ == "__main__":
    run = DependData('login_001')
    print(run.get_depend_data(2))
