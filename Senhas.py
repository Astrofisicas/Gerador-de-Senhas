import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import secrets
import string

# Função para gerar a senha


def gerar_senha():
    try:
        comprimento = int(entry_length.get())
    except ValueError:
        messagebox.showwarning(
            "Erro", "Por favor, insira um número válido para o comprimento da senha.")
        return

    caracteres = ''
    if var_uppercase.get():
        caracteres += string.ascii_uppercase
    if var_lowercase.get():
        caracteres += string.ascii_lowercase
    if var_digits.get():
        caracteres += string.digits
    if var_punctuation.get():
        caracteres += string.punctuation

    if caracteres == '':
        messagebox.showwarning(
            "Erro", "Selecione pelo menos uma categoria de caracteres!")
        return

    senha = ''.join(secrets.choice(caracteres) for _ in range(comprimento))
    entry_password.delete(0, tk.END)
    entry_password.insert(0, senha)

# Função para copiar a senha para a área de transferência


def copiar_senha():
    senha = entry_password.get()
    if senha:
        root.clipboard_clear()
        root.clipboard_append(senha)
        messagebox.showinfo(
            "Copiado", "Senha copiada para a área de transferência!")
    else:
        messagebox.showwarning("Erro", "Nenhuma senha gerada para copiar!")


# Configuração da janela principal
root = tk.Tk()
root.title("Gerador de Senhas")
root.geometry("400x300")

# Estilo ttk
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))

# Título
label_title = ttk.Label(
    root, text="Gerador de Senhas", font=("Helvetica", 16))
label_title.pack(pady=10)

# Entrada para o comprimento da senha
frame_length = ttk.Frame(root)
frame_length.pack(pady=5)
label_length = ttk.Label(frame_length, text="Comprimento da Senha:")
label_length.pack(side=tk.LEFT)
entry_length = ttk.Entry(frame_length, width=5)
entry_length.pack(side=tk.LEFT, padx=5)

# Opções de caracteres
frame_options = ttk.Frame(root)
frame_options.pack(pady=5)
var_uppercase = tk.BooleanVar(value=True)
var_lowercase = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_punctuation = tk.BooleanVar(value=True)
check_uppercase = ttk.Checkbutton(
    frame_options, text="Letras Maiúsculas", variable=var_uppercase)
check_lowercase = ttk.Checkbutton(
    frame_options, text="Letras Minúsculas", variable=var_lowercase)
check_digits = ttk.Checkbutton(
    frame_options, text="Dígitos", variable=var_digits)
check_punctuation = ttk.Checkbutton(
    frame_options, text="Símbolos", variable=var_punctuation)
check_uppercase.grid(row=0, column=0, padx=5, pady=2)
check_lowercase.grid(row=0, column=1, padx=5, pady=2)
check_digits.grid(row=1, column=0, padx=5, pady=2)
check_punctuation.grid(row=1, column=1, padx=5, pady=2)

# Campo para mostrar a senha gerada
label_password = ttk.Label(root, text="Senha Gerada:")
label_password.pack(pady=5)
entry_password = ttk.Entry(root, width=50)
entry_password.pack(pady=5)

# Botões para gerar a senha e copiar
frame_buttons = ttk.Frame(root)
frame_buttons.pack(pady=20)
btn_generate = ttk.Button(
    frame_buttons, text="Gerar Senha", command=gerar_senha)
btn_generate.pack(side=tk.LEFT, padx=10)
btn_copy = ttk.Button(frame_buttons, text="Copiar Senha", command=copiar_senha)
btn_copy.pack(side=tk.LEFT, padx=10)

# Loop principal
root.mainloop()
