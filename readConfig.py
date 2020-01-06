import os
import configparser
import datetime

path = os.path.split(os.path.realpath(__file__))[0]
config_file_path = os.path.join(path,'config.txt')
config = configparser.ConfigParser()
config.read(config_file_path,encoding='utf-8')

class ReadConfig():
    def get_http(self,name):
        value = config.get('HTTP',name)
        return value

    def get_email(self,name):
        value = config.get('EMAIL',name)
        return value

if __name__ == "__main__":
    print('HTTP中的baseurl值为：',ReadConfig().get_http('baseurl'))
    print('EMAIL中的baseurl值为：',ReadConfig().get_email('on_off'))
    print(str(datetime.datetime.now())[0:19])