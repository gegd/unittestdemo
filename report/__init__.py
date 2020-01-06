import os
url = '/usr/local/python3/bin/python3'
current_path = os.getcwd()
report_path = os.path.join(current_path,'report')
print(report_path)
print(os.path.abspath(report_path))
print(os.path.basename(report_path))
print(os.path.dirname(report_path))
print(os.path.split(os.path.realpath(__file__))[0])