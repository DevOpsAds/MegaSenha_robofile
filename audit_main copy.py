import tkinter as tk
from tkinter import filedialog
import pandas as pd

# Função para carregar os dados de um arquivo de texto
def load_data():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Supondo que o arquivo seja um CSV ou TXT com as transações bancárias
        data = pd.read_csv(file_path)
        return data
    else:
        return None

# Função para salvar o DataFrame em um arquivo CSV
def save_to_csv(df):
    if df is not None:
        save_path = filedialog.asksaveasfilename(defaultextension=".csv")
        df.to_csv(save_path, index=False)
        print("Arquivo salvo com sucesso!")
    else:
        print("Nenhum dado para salvar.")

# Função para processar os dados (placeholder para lógica de análise)
def process_data(data):
    # Adicione aqui a lógica de análise de dados
    # Por exemplo: identificar transações recorrentes, altos valores, etc.
    processed_data = data  # Esta linha é apenas um placeholder
    return processed_data

# Função chamada quando o botão de carregar é pressionado
def on_load_pressed():
    data = load_data()
    if data is not None:
        processed_data = process_data(data)
        save_to_csv(processed_data)

# Configuração da interface gráfica Tkinter
root = tk.Tk()
root.title("Analisador de Extrato Bancário")

load_button = tk.Button(root, text="Carregar Dados", command=on_load_pressed)
load_button.pack(pady=20)

root.mainloop()
