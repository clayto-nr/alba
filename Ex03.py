from tkinter import *

janela = Tk()

rotulo = Label(janela, text="Olá, Mundo!")
rotulo.grid(row=0, column=0)

rotulo2 = Label(janela, text="Tudo bem?")
rotulo2.grid(row=1, column=0)

janela.mainloop()
