from tkinter import *

janela = Tk()

info = "Esse texto será exibido no rótulo em várias linhas."
info2 = """Assim também
é possível
ter várias linhas."""

rotulo = Label(janela, text=info, justify="left")
rotulo.grid(row=0, column=0)

botao_sair = Button(janela)
botao_sair.grid(row=1, column=0)
botao_sair["text"] = "Sair"
botao_sair["width"] = 18
botao_sair["command"] = quit

rotulo2 = Label(janela, text=info2, justify="right")
rotulo2.grid(row=1, column=0)

janela.mainloop()
