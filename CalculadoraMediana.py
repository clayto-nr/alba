import tkinter as tk
from tkinter import messagebox

def somar():
    try:
        resultado = float(campo1.get()) + float(campo2.get())
        campo_resultado.config(state='normal')
        campo_resultado.delete(0, tk.END)
        campo_resultado.insert(0, str(resultado))
        campo_resultado.config(state='disabled')
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos!")

def subtrair():
    try:
        resultado = float(campo1.get()) - float(campo2.get())
        campo_resultado.config(state='normal')
        campo_resultado.delete(0, tk.END)
        campo_resultado.insert(0, str(resultado))
        campo_resultado.config(state='disabled')
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos!")

def multiplicar():
    try:
        resultado = float(campo1.get()) * float(campo2.get())
        campo_resultado.config(state='normal')
        campo_resultado.delete(0, tk.END)
        campo_resultado.insert(0, str(resultado))
        campo_resultado.config(state='disabled')
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos!")

def dividir():
    try:
        valor1 = float(campo1.get())
        valor2 = float(campo2.get())
        if valor2 == 0:
            messagebox.showerror("Erro", "Não é possível dividir por zero!")
        else:
            resultado = valor1 / valor2
            campo_resultado.config(state='normal')
            campo_resultado.delete(0, tk.END)
            campo_resultado.insert(0, str(resultado))
            campo_resultado.config(state='disabled')
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos!")

janela = tk.Tk()
janela.title("Calculadora")

campo1 = tk.Entry(janela)
campo1.pack()

campo2 = tk.Entry(janela)
campo2.pack()

campo_resultado = tk.Entry(janela, state='disabled')
campo_resultado.pack()

botao_somar = tk.Button(janela, text="Soma", command=somar)
botao_somar.pack()

botao_subtrair = tk.Button(janela, text="Subtração", command=subtrair)
botao_subtrair.pack()

botao_multiplicar = tk.Button(janela, text="Multiplicação", command=multiplicar)
botao_multiplicar.pack()

botao_dividir = tk.Button(janela, text="Divisão", command=dividir)
botao_dividir.pack()

janela.mainloop()
