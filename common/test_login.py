import unittest
from send_request import RequestAction
import HTMLTestRunner
import os
import json
from unittest import mock
from mock_demo import mock_test
import time

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.run = RequestAction()
    def test_001_login(self):
        url = 'http://10.1.60.111:8000/login'
        data = {
            'username':'gegd',
            'password':'111111'
        }
        
        response_data = self.run.run_main(url,'POST',data)
        response_data_dict = json.loads(response_data)
        self.assertEqual(response_data_dict['resCode'],'200')
        globals()['orderid'] = response_data_dict['data'][0]['OrderId']
    def test_002_login(self):
        url = 'http://10.1.60.111:8000/payment'
        data = {
            'orderid':orderid,
            'recename':'666666',
            'recephone':'ligs',
            'receaddr':'666666'
        }
        response_data = self.run.run_main(url,'POST',data)
        response_data_dict = json.loads(response_data)
        self.assertEqual(response_data_dict['resCode'],'200')

if __name__ == "__main__":
    file_path = os.getcwd()
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    print(now)
    report_path = os.path.join(file_path,'report','report_' + now + '.html')
    with open(report_path,'wb') as fp:
        suite = unittest.TestSuite()
        suite.addTest(TestLogin('test_001_login'))
        suite.addTest(TestLogin('test_002_login'))
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='自动化测试报告')
        runner.run(suite)
        # unittest.TextTestRunner().run(suite)
