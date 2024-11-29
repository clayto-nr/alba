import tkinter as tk
from tkinter import messagebox

def verificar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    if usuario == "admin" and senha == "1234":
        messagebox.showinfo("Login", "Acesso permitido")
    else:
        messagebox.showerror("Login", "Acesso negado")

janela = tk.Tk()
janela.title("Tela de Login")

campo_usuario = tk.Entry(janela)
campo_usuario.pack()
campo_usuario.insert(0, "USER")

campo_senha = tk.Entry(janela, show="*")
campo_senha.pack()
campo_senha.insert(0, "SENGA")

botao_entrar = tk.Button(janela, text="Entrar", command=verificar_login)
botao_entrar.pack()

janela.mainloop()
