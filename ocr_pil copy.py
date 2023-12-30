from PIL import Image
import pytesseract

# Defina o caminho para o executável tesseract no seu sistema
# Somente necessário se o tesseract não estiver no seu PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Função para realizar OCR em uma imagem
def ocr_from_image(image_path):
    # Abre a imagem para leitura
    img = Image.open(image_path)
    
    # Usa o pytesseract para fazer OCR na imagem
    text = pytesseract.image_to_string(img, lang='por')  # Use 'por' para português
    
    return text

# Exemplo de uso
# Substitua 'path_to_image.jpg' pelo caminho para a sua imagem de extrato bancário
extracted_text = ocr_from_image('/media/joao/Salmo5,13/pro/script.py/automacoes/Auditoria/Programa/imagens/Captura de tela de 2023-12-29 14-47-44.png')
print(extracted_text)

# Aqui você pode implementar lógicas adicionais para processar o texto extraído
