from tkinter import PhotoImage, Tk

window = Tk()

from GUI import GUI

gui = GUI(window)


p1 = PhotoImage(file='images\\items\icon.png')

window.iconphoto(False, p1)
window.title("Inventtle")
window.resizable(False, False)
window.mainloop()