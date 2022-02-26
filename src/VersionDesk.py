from tkinter import Tk

from easygui import diropenbox

from Main import Main

if __name__ == '__main__':
    try:

        pdfs = diropenbox()

        view = Tk()

        app = Main(view, pdfs)

        app.mapping_elements()

        view.mainloop()

    except Exception as error:
        exit()
