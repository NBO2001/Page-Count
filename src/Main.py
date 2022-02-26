# -*- coding: utf-8 -*-

from os import walk
from sys import exit, platform
from tkinter import *
from tkinter import ttk

from PyPDF2 import PdfFileReader


class Main:
    def __init__(self, master, location):
        self.inst = master
        self.location = location
        self.totPages = 0
        self.create_structure()
        self.add_elements()

    def create_structure(self):

        self.inst.title('NBO2022 - Page Count')
        self.inst.geometry('400x400')

        self.my_informations_frame = Frame(self.inst)
        self.my_informations_frame.pack()

        self.my_button = ttk.Button(
            self.my_informations_frame, text='Sair', command=self.inst.destroy
        )

        self.my_informations = ttk.Treeview(self.my_informations_frame)
        self.my_informations['columns'] = ('file_name', 'pages_value')

        self.my_informations.column('#0', width=0, stretch=NO)
        self.my_informations.column('file_name', anchor=W, width=300)
        self.my_informations.column('pages_value', anchor=CENTER, width=80)

        self.my_informations.heading('#0', text='', anchor=CENTER)
        self.my_informations.heading('file_name', text='Nome', anchor=W)
        self.my_informations.heading(
            'pages_value', text='Total', anchor=CENTER
        )

        self.myLabel = ttk.Label(self.my_informations_frame, text=(f''))

    def add_elements(self):
        self.my_informations.pack()
        self.myLabel.pack()
        self.my_button.pack()

    def insert_data(self, file, pages, idd_value):

        self.my_informations.insert(
            parent='',
            index='end',
            iid=idd_value,
            text='',
            values=(file, pages),
        )

        self.inst.update()

        return idd_value + 1

    def set_totalPages(self, pages):
        self.totPages = pages
        self.myLabel['text'] = f'Total de paginas = {pages}'

    def get_totalPages(self):
        return self.totPages

    def pdf_pages(self, file):
        # Function reader file pdf end return sum pages
        document = PdfFileReader(file)
        return document.getNumPages()

    def verify_the_file_is_pdf(self, file):

        # Verifica se o arquivo é um pdf, se for, retorna True, caso contrário, retorna False

        if not isinstance(file, str):
            raise TypeError(f'Erro ao receber um valor que não é uma string')

        file_array = file.split('.')

        if file_array[len(file_array) - 1].upper() != 'PDF':
            return False
        else:
            return True

    def convert_away(self, road):
        # Altera a / para \\ quando no win
        if (platform).upper() == 'LINUX':
            return road
        else:
            list_road = road.split('/')
            return '\\'.join(list_road)

    def mapping_elements(self):
        idd_value = 0

        for path, _, files in walk(self.convert_away(self.location)):

            for file in files:

                if self.verify_the_file_is_pdf(file):

                    finalPath = self.convert_away(f'{path}/{file}')
                    idd_value = self.insert_data(
                        file, self.pdf_pages(finalPath), idd_value
                    )
                    self.set_totalPages(
                        self.get_totalPages() + self.pdf_pages(finalPath)
                    )
