from Main import Main

from tkinter import Tk

try:
    
    view = Tk()

    app = Main(view, "./")

    app.mapping_elements()
    
    view.mainloop()

except Exception as error:
    exit()