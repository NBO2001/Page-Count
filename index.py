# -*- coding: utf-8 -*-

import sys
import os
from easygui import diropenbox
from PyPDF2 import PdfFileReader
from tkinter import *
from  tkinter import ttk

try:
    
    if((sys.platform).upper() == "LINUX"):
        folders_separator = "/"
    else:
        folders_separator = "\\"
    
    pdfs = diropenbox()

    totPages = 0

    view = Tk()
    view.title("NBO2001 - Page Count")
    view.geometry('400x400')

    my_informations_frame = Frame(view)
    my_informations_frame.pack()

    my_button = ttk.Button(my_informations_frame, text="Sair", command=view.destroy)


    my_informations = ttk.Treeview(my_informations_frame)
    my_informations['columns'] = ('file_name', 'pages_value')

    my_informations.column("#0", width=0,  stretch=NO)
    my_informations.column("file_name", anchor=W, width=300)
    my_informations.column("pages_value", anchor=CENTER, width=80)

    my_informations.heading("#0",text="",anchor=CENTER)
    my_informations.heading('file_name', text="Nome", anchor=W)
    my_informations.heading('pages_value', text="Total", anchor=CENTER)


    idd_value = 0
    for path, subPath, files in os.walk(pdfs):
        
        for file in files:
            fileOny = file.split(".")
            if len(fileOny) == 2 and (fileOny[1]).upper() == "PDF":
                finalPath = (f'{path}{folders_separator}')

                finalPath = (f'{finalPath}{file}')
                document = PdfFileReader(finalPath)
                pages = document.getNumPages()
                totPages = totPages + pages
                my_informations.insert(parent='', index='end', iid=idd_value, text='',
                values=(file, pages))
                idd_value = idd_value + 1

    myLabel = ttk.Label(my_informations_frame, text=(f'Total de paginas = {totPages}'))

    my_informations.pack()
    myLabel.pack()
    my_button.pack()

    view.mainloop()
except:
    sys.exit()