import shutil
from docxtpl import DocxTemplate
from pathlib import Path
import configparser
import os
from docxcompose.composer import Composer
from docx import Document as Document_compose


def wordTemplate():
    i = 0
    single_diploma = []

    lists_path = Path('lists')
    pattern_path = Path('patterns')
    diploma_path = Path('diplomas')
    spiski = []

    def spisok():
        for file in os.listdir(lists_path):
            spiski.append(file)

    class Config:
        config = configparser.ConfigParser()
        config.read('config.ini', encoding='UTF-8')
        date1 = config.get('Config', 'date1')
        date2 = config.get('Config', 'date2')
        director = config.get('Config', 'director')
        year = config.get('Config', 'year')

    spisok()
    shutil.rmtree("diplomas", ignore_errors=True)
    os.mkdir("diplomas")
    for gruppa in spiski:
        f = open(lists_path / gruppa, 'r', encoding='UTF-8')
        prog = f.readline()
        name_len = len(prog)
        for line in f:
            if name_len < 85:
                doc = DocxTemplate(pattern_path / 'base_1.docx')
            elif (name_len > 84) and (name_len < 127):
                doc = DocxTemplate(pattern_path / 'base_2.docx')
            elif (name_len > 126) and (name_len < 161):
                doc = DocxTemplate(pattern_path / 'base_3.docx')
            elif name_len > 161:
                doc = DocxTemplate(pattern_path / 'base_4.docx')

            context = {'fio': line,
                       'date1': Config.date1,
                       'date2': Config.date2,
                       'kvant': str(prog),
                       'director': Config.director,
                       'year': Config.year}
            doc.render(context)
            doc.save("diploma_" + str(i) + ".docx")
            shutil.move("diploma_" + str(i) + ".docx", "diplomas")
            diploma_path = Path('diplomas/diploma_' + str(i) + '.docx')
            single_diploma.append(diploma_path)
            i += 1
        f.close()

    del single_diploma[0]

    def combine_all_docx(filename_master, files_list):
        number_of_sections = len(files_list)
        master = Document_compose(filename_master)
        composer = Composer(master)
        for i in range(0, number_of_sections):
            doc_temp = Document_compose(files_list[i])
            composer.append(doc_temp)
        composer.save(r"C:\Users\Student.QUANTORIUM70\Documents\document\combined_file.docx")
