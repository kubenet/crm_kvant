import shutil
from docxtpl import DocxTemplate
from pathlib import Path
import configparser
import os
import openpyxl, openpyxl.utils


def excelDogovor(group):
    lists_path = Path('lists')

    wb = openpyxl.load_workbook(lists_path / group)
    sheet = wb.active