import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb

# Cria janela
window = tk.Tk()
window.title('Calculadora Fatorial')
window.geometry('450x450')
window.configure(bg='#f0f0f0')  

# Título
titulo = tk.Label(window, text='Calculadora Fatorial', font=('Helvetica', 20, 'bold'), bg='#f0f0f0', fg='#4a4a4a')
titulo.pack(pady=20)

# Entrada do usuário
entrada = ttk.Entry(window, font=('Helvetica', 16), justify='center',  width=10)
entrada.pack(pady=20)

# Lógica do programa
def calcular_fatorial():
    try:
        numero = int(entrada.get())  # Obtém o número da entrada
        if numero < 0:
            resultado_label.config(text='Por favor, insira um número não negativo.')
            return
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i  # Calcula o fatorial
        resultado_label.config(text=f'O fatorial de {numero} é {resultado:,}')  # Atualiza o texto do label.
    except ValueError:
        resultado_label.config(text='Por favor, insira um número válido.')


botao = ttk.Button(window, text='Calcular Fatorial',command=calcular_fatorial)
botao.pack(pady=10)

# Label de resultado
resultado_label = tk.Label(window, text='', font=('Helvetica', 16), bg='#f0f0f0', fg='#4a4a4a')
resultado_label.pack(pady=20)


style = ttk.Style()
style.configure('TButton', font=('Helvetica', 14), padding=10, background='black', foreground='black')
style.map('TButton', background=[('active', '#4cae4c')])  # Cor ao passar o mouse

# Inicia o loop da interface
window.mainloop()
