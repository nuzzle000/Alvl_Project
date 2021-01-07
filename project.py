import tkinter
from tkinter import tk
mainWin = tkinter.Tk()
mainWin.title("Untitled")
mainWin.geometry("600x600")

btn1 = tkinter.Button(mainWin, text="Hello").pack()

mainWin.mainloop()