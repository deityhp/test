# import openpyxl
# wb = openpyxl.load_workbook("2018.xlsx")
# sheet = wb.worksheets[0]
# print(sheet.cell(1,1))
# 
# for x in range(1,20):
#     for y in range(1,8):
#         sheet.cell(x,y).value = ""
# 
# 
# 
# for i in range(1,20):
#     rows = sheet[i]
# 
#     for row in rows:
#         print(row.value)
#         print(row)
import os
print (os.path.abspath('.'))