from tkinter import Tk

window = Tk()

from GUI import GUI

gui = GUI(window)

window.resizable(False, False)
window.mainloop()