import time
from PIL import Image
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





        
def load_image_and_extract_text(file_path):
    try:
        # Aguardar um momento para garantir que o arquivo esteja totalmente escrito
        time.sleep(1)

        # Tenta abrir a imagem
        img = Image.open(file_path)
        obj_bruto = pytesseract.image_to_string(img, lang='por')
        process_extracted_text(obj_bruto)
      
    except IOError as e:
        return f"Erro ao abrir a imagem no caminho: {file_path}. Erro: {e}"





def process_extracted_text(text):

    text = re.sub(r',(\d{2})(\d)', r',\1-', text)
    text = re.sub(r',\s+', ',', text)
    print(text)
    # Regex para datas, descrições, códigos e valores
    pontos = re.findall(r'\.', text)
    cont_pontos = len(pontos)

    # Contar vírgulas
    virgulas = re.findall(r',', text)
    cont_virgulas = len(virgulas)

    # Contar barras
    barras = re.findall(r'/', text)
    cont_barras = len(barras)

    # Contar espaços em branco entre barras
    espacos_entre_barras = re.findall(r'/(?:(?!\n|/).)*\s(?:(?!\n|/).)*/', text)
    cont_espacos_entre_barras = sum(len(re.findall(r'\s', match)) for match in espacos_entre_barras)

    # Contar números entre pontos
    numeros_entre_pontos = re.findall(r'\.(?:\D*?(\d)\D*?)*\.', text)
    cont_numeros_entre_pontos = sum(len(match) for match in numeros_entre_pontos)

    # Contar espaços em branco entre pontos
    espacos_entre_pontos = re.findall(r'\.(?:[^.\S]*?(\s)[^.\S]*?)*\.', text)
    cont_espacos_entre_pontos = sum(len(match) for match in espacos_entre_pontos)

    # Contar espaços entre uma barra e um sinal de menos
    espacos_entre_barra_e_menos = re.findall(r'/[^/-]*?\s[^/-]*?-', text)
    cont_espacos_entre_barra_e_menos = sum(len(re.findall(r'\s', match)) for match in espacos_entre_barra_e_menos)

    # Contar espaços entre uma vírgula e o próximo ponto
    espacos_entre_virgula_e_ponto = re.findall(r',[^,.\s]*?\s[^,.\s]*?\.', text)
    cont_espacos_entre_virgula_e_ponto = sum(len(re.findall(r'\s', match)) for match in espacos_entre_virgula_e_ponto)

    espacos = re.findall(r' ', text)
    contador = len(espacos)
    quebras_de_linha = re.findall(r'\n', text)
    contadorquebrada = len(quebras_de_linha)
    textSemespso = re.sub(r'\s+', '', text)
    date_pattern = r"(\d{2}/\d{2})"
    description_pattern = r"([A-Z][^\d]+?)(?=\d{2}\.\d+\.\d+|\d{2}/\d{2}|$)"
    code_pattern = r"(\d{2}\.\d+\.\d+\.\d+|\d{2}\.\d+\.\d+)"
    value_pattern = r"(\d{1,3},\d{2})(?=\s|$)"
    value_patternno = r"(\d+\.\d+,\d+|\d+,\d+)(?=[^-])" 
    # Encontrando os padrões no texto
    dates = re.findall(date_pattern, text)
    descriptions = re.findall(description_pattern, text)
    codes = re.findall(code_pattern, text)
    values = re.findall(value_pattern, text)
    
    regex = r"\d+,\d{3}"
    # Procurar pela regex no texto
   


    # Encontrando os valores usando um loop for ao invés de findall
    values = []
    for match in re.finditer(value_patternno, text):
        # Regex para encontrar números com três algarismos após a vírgula


        # Excluindo os padrões que terminam com hífen
        if not match.group(0).endswith('-') and len(match.group(0).split(',')[0]) <= 5:
                      # Excluindo os padrões que terminam com hífen
        # Se o número tiver exatamente 3 casas decimais, remover as 2 últimas
             if re.search(regex, match.group(0)):
                #parte_inteira, parte_decimal = value.split(',')
                #Svalue = parte_inteira + ',' + parte_decimal[0]
                #indice = match.group.index(match.group(0))
                # Separar a parte inteira e decimal
                partes = match.group(0).split(',')
             

                # Verificar se a parte decimal tem 3 algarismos
                if len(partes[1]) == 3:
                    # Modificar o número para manter apenas o primeiro algarismo decimal
                    numero_modificado = partes[0] + ',' + partes[1][0]

                    print("Número original:", match.group(0))
                    print("Número modificado:", numero_modificado)
                    if len(numero_modificado.split(',')[1]) == 1:
                        value = "-" + match.group(0)
                        values.append(value)


             elif len(match.group(0).split(',')[1]) == 1:
                value = "-" + match.group(0)
                values.append(value)
             else:
                values.append(match.group(0))
        extracted_data = []
        for i, desc in enumerate(descriptions):
            data_entry = {"Valor": None}
            if i < len(values):
                data_entry["Valor"] = values[i]
            extracted_data.append(data_entry)

    # Removendo espaços em branco e ajustando descrições
    descriptions = [desc.strip().replace('\n', ' ') for desc in descriptions]

    # Ajustar índices para valores e códigos com base na data
    # Assumindo que cada data se refere a uma transação e ignorando datas extras
    data_index = 0
    extracted_data = []
 
    for i in range(len(descriptions)):
        # Se uma descrição for encontrada sem uma data correspondente, use a última data disponível
        if data_index >= len(dates):
            data_index = len(dates) - 1

        value_index = i if i < len(values) else None
        code_index = i if i < len(codes) else None

        # Criar dicionário de dados
        data = {
            "Data": dates[data_index],
            "Descrição": descriptions[i],
            "Código": codes[code_index] if code_index is not None else None,
            "Valor": values[value_index] if value_index is not None else None
        }
        extracted_data.append(data)

        # Incrementar o índice da data somente se uma data foi usada para uma descrição
        if i < len(codes) and i < len(values):
            data_index += 1
    for data in extracted_data:
        print(data)

    return extracted_data
