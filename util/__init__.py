# import xlrd
# import os

# filepath = os.path.join(os.getcwd(),'testfile','EHR_LOOKUP_CODES.xls')
# cls = []
# data = xlrd.open_workbook(filepath)
# sheet = data.sheet_by_index(0)
# print(sheet.nrows)
# print(sheet.row_values(1))
# for i in range(sheet.nrows):
#     cls.append(sheet.row_values(i))

# print(cls)