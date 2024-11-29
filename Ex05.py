from tkinter import *

janela = Tk()

rotulo = Label(janela, text="Olá, Mundo!")

rotulo.grid(row=0, column=0)
rotulo["font"] = ("Arial", 18, "bold", "italic")  
rotulo["fg"] = "red"  
rotulo["bg"] = "white" 

janela.mainloop()
