import openpyxl, openpyxl.utils

wb = openpyxl.load_workbook('excelList.xlsx')

sheet = wb.active
print(sheet.title)
print(sheet['A1'].value)
print(sheet.max_column)