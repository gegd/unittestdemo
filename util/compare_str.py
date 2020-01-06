import json


def is_in_result(str1,res):
    flag = None
    if str1 in res:
        flag = True
    else:
        flag =False
    return flag

def is_equal(res1,res2):
    if isinstance(res1,dict):
        res1 = json.dumps(res1)
        print(res1)
    if isinstance(res2,dict):
        res2 = json.dumps(res2)
        print(res2)
    return is_in_result(res1,res2)


a = {'rr':'111','gg':'222'}
b = '{"rr": "111", "gg": "222"}'
print(type(b))

c = is_equal(a,b)
print(c)
