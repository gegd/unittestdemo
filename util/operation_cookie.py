import sys
import os
sys.path.append(os.getcwd())
import requests
import json

from util.operation_json import OperationJson

class OperationCookie():
    def __init__(self,response):
        self.response = response
        self.oper_json = OperationJson()

    def get_cookie(self):
        final_cookies = {}
        cookie = self.response.cookies
        cookies = requests.utils.dict_from_cookiejar(cookie)
        for k in cookies:
            cookies = k + '=' + cookies[k]
        final_cookies['Cookie'] = cookies
        print(cookie)
        print(final_cookies)
        return final_cookies

    def write_cookie(self):
        cookie_json = self.get_cookie()
        self.oper_json.write_cookie_json(cookie_json)



if __name__ == "__main__":
    login_url = 'http://10.0.20.53:8080/login'
    login_data = {
        'userName':'rm',
        'password':'rm123456'
    }
    res = requests.post(login_url,login_data)
    oper_cookie = OperationCookie(res)
    oper_cookie.write_cookie()


# url = 'http://10.0.20.53:8080/jobinfo/trigger'
# data = {
#     'id':'201',
#     'executorParam':'aaa'
# }
# res = requests.post(url=url,data=data,cookies=cookies).json()
# print(json.dumps(res))

