from unittest import mock

def mock_test(request_method,url,request_data,method,response_data):
    request_method = mock.Mock(return_value=response_data)
    res = request_method(url,method,request_data)
    return res