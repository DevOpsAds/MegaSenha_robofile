import tkinter as tk
from tkinter import filedialog
from PIL import Image
import pytesseract

# Função para realizar OCR em uma imagem
def ocr_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang='por')
    return text

# Função para carregar a imagem e mostrar o texto extraído
def load_image_and_extract_text():
    file_path = filedialog.askopenfilename()
    if file_path:
        extracted_text = ocr_from_image(file_path)
        text_label.config(text=extracted_text)

# Configuração da janela principal
root = tk.Tk()
root.title("OCR com Tkinter e Tesseract")

# Botão para carregar a imagem
load_button = tk.Button(root, text="Carregar Imagem", command=load_image_and_extract_text)
load_button.pack()

# Label para mostrar o texto extraído
text_label = tk.Label(root, text="", wraplength=300)
text_label.pack()

# Executar a janela
root.mainloop()


import tkinter as tk
from tkinter import filedialog
from PIL import Image
import pytesseract
import re

# Função para realizar OCR em uma imagem
def ocr_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang='por')
    return text

# Função para processar e organizar os dados extraídos
def process_extracted_text(text):
    # Regex para datas, nomes de transferência, códigos e valores
    date_pattern = r"\d{2}/\d{2}/\d{4}"  # Exemplo: 29/12/2023
    transfer_name_pattern = r"(Nome da Transferência: \w+)"  # Exemplo: Nome da Transferência: TransferXYZ
    transfer_code_pattern = r"(Código da Transferência: \d+)"  # Exemplo: Código da Transferência: 123456
    value_pattern = r"R\$\s*\d+,\d{2}"  # Exemplo: R$ 100,00

    # Encontrando os padrões no texto
    dates = re.findall(date_pattern, text)
    transfer_names = re.findall(transfer_name_pattern, text)
    transfer_codes = re.findall(transfer_code_pattern, text)
    values = re.findall(value_pattern, text)

    # Organizar os dados (aqui você pode ajustar conforme a estrutura do seu print)
    extracted_data = []
    for i in range(len(dates)):
        data = {
            "Data": dates[i],
            "Nome da Transferência": transfer_names[i] if i < len(transfer_names) else None,
            "Código da Transferência": transfer_codes[i] if i < len(transfer_codes) else None,
            "Valor": values[i] if i < len(values) else None
        }
        extracted_data.append(data)

    return extracted_data

# Função para carregar a imagem e mostrar os dados organizados
def load_image_and_process_data():
    file_path = filedialog.askopenfilename()
    if file_path:
        extracted_text = ocr_from_image(file_path)
        organized_data = process_extracted_text(extracted_text)
        
        # Exibir os dados organizados
        display_text = "\n".join(str(data) for data in organized_data)
        text_label.config(text=display_text)

# Configuração da janela principal
root = tk.Tk()
root.title("OCR e Processamento de Dados Bancários")

# Botão para carregar a imagem
load_button = tk.Button(root, text="Carregar Imagem e Processar Dados", command=load_image_and_process_data)
load_button.pack()

# Label para mostrar os dados organizados
text_label = tk.Label(root, text="", wraplength=500)
text_label.pack()

# Executar a janela
root.mainloop()

extracted_text = ocr_from_image('caminho_para_imagem.jpg')
organized_data = process_extracted_text(extracted_text)

# Imprimir os dados organizados
for data in organized_data:
    print(data)

