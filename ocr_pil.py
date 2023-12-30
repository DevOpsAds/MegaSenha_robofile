import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageFilter, ImageEnhance
import pytesseract


import re


from ler_o_bruto_organizado_Obj import tratamento_dados_brutos_organizado_white_pag
# Função para realizar OCR em uma imagem
def ocr_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, lang='por')
        return text
    except IOError as e:
        return f"Erro ao abrir a imagem no caminho: {image_path}. Erro: {e}"



def oScr_from_image(image_path):
    try:
        # Abre a imagem
        img = Image.open(image_path)
        
        # Converte para escala de cinza
        img = img.convert('L')
        
        # Aplica thresholding para tornar a imagem em preto e branco
        threshold = 200
        img = img.point(lambda p: p > threshold and 255)
        
        # Aumenta o contraste da imagem
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(2)
        
        # Redimensiona a imagem para aumentar a clareza do texto
        img = img.resize([2 * dim for dim in img.size], Image.ANTIALIAS)
        
        # Aplica um filtro para suavizar a imagem
        img = img.filter(ImageFilter.SMOOTH)
        
        # Realiza OCR na imagem processada
        text = pytesseract.image_to_string(img, lang='por')
 
        return text
    
    except IOError as e:
        return f"Erro ao abrir a imagem no caminho: {image_path}. Erro: {e}"


# Função para carregar a imagem, processar e mostrar os dados
def noload_image_and_process_data():
    file_path = filedialog.askopenfilename()
    if file_path:
        extracted_text = ocr_from_image(file_path)
        if extracted_text.startswith("Erro"):
            text_label.config(text=extracted_text)
            print(display_text)
        else:
            organized_data = process_extracted_text(extracted_text)
            display_text = "\n".join(str(data) for data in organized_data)
            text_label.config(text=display_text)
            print(display_text)  # Adiciona o print aqui
brutos="""


"""

def load_image_and_extract_text():
    file_path = filedialog.askopenfilename()
    if file_path:
        extracted_text = ocr_from_image(file_path)
        text_label.config(text=extracted_text)
        print(extracted_text)  # Adiciona o print aqui
        obj_bruto=process_extracted_text(extracted_text)
        print("%%%%%%%%%@@@@@@@@",obj_bruto)
        tratamento_dados_brutos_organizado_white_pag(obj_bruto)
        print(obj_bruto)




def process_extracted_text(text):
    # Lista para armazenar os dados extraídos
    extracted_data = []

    # Split o texto em linhas
    lines = text.split('\n')

     # Regex para datas, descrições, códigos e valores
    date_pattern = r"(\d{2}/\d{2})"
    description_pattern = r"([A-Z].*?)(?=\d{2}\.\d+\.\d+|\d{2}/\d{2}|$)"
    code_pattern = r"(\d{2}\.\d+\.\d+\.\d+|\d{2}\.\d+\.\d+)"
    value_pattern = r"(\d+\.\d+,\d+|\d+,\d+)(?=-|\s)"
    
    # Encontrando os padrões no texto
    dates = re.findall(date_pattern, text)
    descriptions = re.findall(description_pattern, text)
    codes = re.findall(code_pattern, text)
    values = re.findall(value_pattern, text)

    # Removendo espaços em branco e ajustando descrições
    descriptions = [desc.strip().replace('\n', ' ') for desc in descriptions]
    
    # Iterar sobre cada linha do texto
    for line in lines:
        # Ignorar linhas que contêm "SALDO"
        if "SALDO" in line:
            continue

        # Encontrar a data
        date_match = re.search(r'\d{2}/\d{2}', line)
        if date_match:
            current_date = date_match.group()

        # Encontrar o código
        code_match = re.search(r'\d{2}\.\d{5}\.\d', line)
        if code_match:
            current_code = code_match.group()

        # Encontrar o valor
        value_match = re.search(r'\d+\.\d{2,},\d{2}-?', line)
        if value_match:
            current_value = value_match.group().replace('.', '').replace(',', '.')
            if current_value.endswith('-'):
                current_value = '-' + current_value[:-1]

        # Se uma linha não contém "SALDO" mas tem conteúdo, então é uma descrição
        if line and "SALDO" not in line and not date_match and not code_match and not value_match:
            current_description = line

        # Se todos os componentes estão presentes, salvar a transação
        if all([current_date, current_description, current_code, current_value]):
            extracted_data.append({
                'Data': current_date,
                'Descrição': current_description,
                'Código': current_code,
                'Valor': current_value
            })
            # Resetar para a próxima transação
            current_description = None
            current_code = None
            current_value = None
        # Encontrando os padrões no texto
            
        dates = re.findall(date_pattern, text)
        descriptions = re.findall(description_pattern, text)
        codes = re.findall(code_pattern, text)
        values = re.findall(value_pattern, text)

        # Removendo espaços em branco e ajustando descrições
        descriptions = [desc.strip().replace('\n', ' ') for desc in descriptions]  

        # Ajustar índices para valores e códigos com base na data
        value_index = i if i < len(values) else None
        code_index = i if i < len(codes) else None
        
        # Criar dicionário de dados
        data = {
            "Data": date,
            "Descrição": descriptions[i] if i < len(descriptions) else None,
            "Código": codes[code_index] if code_index is not None else None,
            "Valor": values[value_index] if value_index is not None else None
        }
        extracted_data.append(data)
        
    return extracted_data
    print ("$$$$$$",extracted_data)
    return extracted_data

# Configuração da janela principal
root = tk.Tk()
root.title("OCR e Processamento de Dados Bancários")

# Botão para carregar a imagem
load_button = tk.Button(root, text="Carregar Imagem e Processar Dados", command=load_image_and_extract_text)
load_button.pack()

# Label para mostrar os dados organizados
text_label = tk.Label(root, text="", wraplength=500)
text_label.pack()

# Executar a janela
root.mainloop()
