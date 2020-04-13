from pathlib import Path
import openpyxl, openpyxl.utils

lists_path = Path('lists')
group = 'IT_project.xlsx'
students = []


def xlStudFiller(group):
    wb = openpyxl.load_workbook(lists_path / group)
    students = wb.sheetnames
    return students
