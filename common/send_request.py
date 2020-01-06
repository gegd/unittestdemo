import requests
import json




class RequestAction():
   
    def send_post(self,url,data,header=None):
        res = requests.post(url=url,data=data,headers=header).json()
        return json.dumps(res,ensure_ascii=False)

        

    def send_get(self,url,header=None,data=None):
        res = requests.get(url=url,data=data,headers=header,verify=False).text
        res = json.loads(res)
        return json.dumps(res,ensure_ascii=False)

    def run_main(self,url,method,data=None,header=None):
        res = None
        if method == 'GET':
            res = self.send_get(url,data,header)
        else:
            res = self.send_post(url,data,header)
        return res

if __name__ == "__main__":
    url = 'http://10.0.20.53:8080/jobinfo/trigger'
    data = {
        'id':'201',
        'executorParam':'aaa'
    }
    # url = 'http://10.0.20.53:8080/login'
    # data = {
    #     'userName':'rm',
    #     'password':'rm123456'
    # }
   
    # url = 'http://10.1.60.111:8000/login'
    # data = {
    #     "username":"gegd",
    #     "password":"111111"
    # }
    run = RequestAction()
    res = run.run_main(url,'POST',data)



