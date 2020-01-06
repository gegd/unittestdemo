import os
import json

class OperationJson():
    def __init__(self,file_path=None):
        if file_path == None:
            self.file_path = os.path.join(os.getcwd(),'cookie.json')
        else:
            self.file_path = file_path
    
    def get_json_value(self,key):
        fp = open(self.file_path,encoding='utf-8')
        json_data = json.load(fp)
        return json_data[key]

    def read_cookie_json(self):
        with open(self.file_path,'r') as fp:
            cookie_json = json.load(fp)
            return cookie_json

    def write_cookie_json(self,cookie_json):
        with open(self.file_path,'w') as fp:
            json.dump(cookie_json,fp)


if __name__ == "__main__":
    operation_json = OperationJson(os.path.join(os.getcwd(),'cookie.json'))
    print(operation_json.read_cookie_json())