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
