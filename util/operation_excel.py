import sys
import os
sys.path.append(os.getcwd())
import xlrd
from common.excel_col import ExcelCol
from util.operation_json import OperationJson
from xlutils.copy import copy
import json

class OperationExcel():
    def __init__(self,file_path=None,sheet_id=None):
        if file_path == None:
            file_path = os.path.join(os.getcwd(),'testfile','case.xlsx')
            sheet = xlrd.open_workbook(file_path)
            self.data = sheet.sheet_by_index(0)
        else:
            sheet = xlrd.open_workbook(file_path)
            self.data = sheet.sheet_by_index(sheet_id)

    def get_nrows(self):
        return self.data.nrows

    def get_cell_value(self,row,col):
        cell_value = self.data.cell_value(row,col)
        return cell_value

    def write_result(self,row,col,res):
        file_path = os.path.join(os.getcwd(),'testfile','case.xlsx')
        old_sheet = xlrd.open_workbook(file_path)
        copy_data = copy(old_sheet)
        copy_sheet = copy_data.get_sheet(0)
        copy_sheet.write(row,col,res)
        copy_data.save(file_path)

    #获取整行数据
    def get_row_data(self,row):
        return self.data.row_values(row)

    # 获取整列数据
    def get_col_datas(self,col=None):
        if col != None:
            cols = self.data.col_values(col)
        else:
            cols = self.data.col_values(0)
        return cols

    



if __name__ == "__main__":
    run = OperationExcel()
    print(run.get_nrows())
    print(run.get_col_datas(0))