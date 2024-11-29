from tkinter import *

janela = Tk()

logo = PhotoImage(file="logo.png")

rotulo2 = Label(janela, image=logo)
rotulo2.grid(row=0, column=1)

janela.mainloop()
