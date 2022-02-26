from tkinter import Tk

from Main import Main

if __name__ == '__main__':

    try:

        view = Tk()

        app = Main(view, './')

        app.mapping_elements()

        view.mainloop()

    except Exception as error:
        exit()
