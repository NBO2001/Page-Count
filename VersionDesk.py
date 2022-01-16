from Main import Main

from tkinter import Tk

from easygui import diropenbox

try:
    
    pdfs = diropenbox()

    view = Tk()

    app = Main(view, pdfs)

    app.mapping_elements()
    
    view.mainloop()

except Exception as error:
    exit()