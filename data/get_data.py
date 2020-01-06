import xlrd
import os
import sys
sys.path.append(os.getcwd())
from common.excel_col import ExcelCol
from util.operation_excel import OperationExcel
from util.operation_json import OperationJson
from util.operation_db import OperationDB

class GetData():
    def __init__(self,file_path=None,sheet_id=None):
        self.oper_excel = OperationExcel()
        self.oper_json = OperationJson(os.path.join(os.getcwd(),'request_data.json'))

    def get_case_id(self,row):
        col = int(ExcelCol.get_id())
        case_id = self.oper_excel.get_cell_value(row,col)
        return case_id

    def get_nrows(self):
        return self.oper_excel.get_nrows()

    def get_is_run(self,row):
        flag = None
        col = int(ExcelCol.get_is_run())
        is_run = self.oper_excel.get_cell_value(row,col)
        if is_run == 'yes':
            flag = True
        else:
            flag = False
        return flag

    def get_url(self,row):
        col = int(ExcelCol.get_url())
        url = self.oper_excel.get_cell_value(row,col)
        return url

    def get_request_data(self,row):
        col = int(ExcelCol.get_request_data())
        json_key = self.oper_excel.get_cell_value(row,col)
        json_value = self.oper_json.get_json_value(json_key)
        return json_value

    def get_request_method(self,row):
        col = int(ExcelCol.get_request_method())
        request_method = self.oper_excel.get_cell_value(row,col)
        return request_method

    def get_header(self,row):
        col = int(ExcelCol.get_header())
        header = self.oper_excel.get_cell_value(row,col)
        if header == None:
            return None
        else:
            return header

    def get_expect(self,row):
        col = int(ExcelCol.get_expect())
        expect =self.oper_excel.get_cell_value(row,col)
        # expect_db = OperationDB(expect)
        return expect

    def get_depend_key(self,row):
        col = int(ExcelCol.get_field_id())
        depend_key = self.oper_excel.get_cell_value(row,col)
        return depend_key

    def get_field_key(self,row):
        col = int(ExcelCol.get_field_data())
        field_key = self.oper_excel.get_cell_value(row,col)
        return field_key

    def get_field_data_id(self,row):
        col = int(ExcelCol.get_field_data_id())
        field_data_id = self.oper_excel.get_cell_value(row,col)
        return field_data_id

    def write_res(self,row,res):
        col = int(ExcelCol.get_result())
        self.oper_excel.write_result(row,col,res)

    def get_expect_by_case(self,row):
        oper_db = OperationDB(self.get_case_id(row))
        expect_db = oper_db.search_one()
        return expect_db

    # 根据依赖case_id获取到要执行的用例id的行号
    def get_depend_line(self,case_id):
        num = 0
        cols_data = self.get_col_datas()
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num += 1
        return num

    def get_row_values(self,row):
        return self.oper_excel.get_row_data(row)

    # 获取某一列的内容
    def get_col_datas(self,col=None):
        col_datas = self.oper_excel.get_col_datas(col)
        return col_datas
        





if __name__ == "__main__":
    run = GetData()
    print(run.get_nrows())
    print(run.get_url(1))
    print(run.get_request_data(1))
    print(run.get_depend_line('login_001'))