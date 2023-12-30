import tkinter as tk
from tkinter import filedialog
import ocrpil

def load_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        extracted_text = ocrpil.ocr_from_image(file_path)
        print(extracted_text)

root = tk.Tk()
root.title("Carregar Imagem para OCR")

load_image_button = tk.Button(root, text="Carregar Imagem", command=load_image)
load_image_button.pack()

root.mainloop()
