import tkinter as tk
from tkinter import messagebox

def somar():
    try:
        valor1 = float(campo1.get())
        valor2 = float(campo2.get())
        resultado = valor1 + valor2
        campo_resultado.config(state='normal')  
        campo_resultado.delete(0, tk.END)
        campo_resultado.insert(0, str(resultado)) 
        campo_resultado.config(state='disabled')  
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos!")

janela = tk.Tk()
janela.title("Somador")

campo1 = tk.Entry(janela)
campo1.pack()

campo2 = tk.Entry(janela)
campo2.pack()

campo_resultado = tk.Entry(janela, state='disabled')
campo_resultado.pack()

botao_somar = tk.Button(janela, text="Somar", command=somar)
botao_somar.pack()

janela.mainloop()
