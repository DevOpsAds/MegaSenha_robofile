import re
import csv
import os

"""[
        "12/09", "12/09", "12/09", "12/09", "12/09", "12/09", "", 
        "MOBILEPAG TIT 4800148270", "2.96217.1 9427", "1.783,06-",
        "PIX TRANSF ANA LUC", "32.61209.1 9136", "3.500,00-",
        "PIX TRANSF ANA LUC", "32.98933.1 9126", "3.500,00-",
        "EST PIX TF ANA LUCIA", "76.12029.1 9026", "3.500,00",
        "EST PIX TE ANA LUCIA", "76.75359.1 9122", "3.500,00",
        "RES APLIC AUT MAIS", "74.09117.8", "10.788,27",
        "REND PAGO APLIC AUT MAIS", "74.09117.8", "0,03"
    ]"""
def tratamento_dados_brutos_white_pag(dados):
    # Dados brutos fornecidos
    dados_brutos = dados 

    # Inicializar lista para transações
    transacoes = []

    # Regex para identificar as datas
    data_regex = r"\d{2}/\d{2}"

    # Variável para manter a data atual
    data_atual = ""

    # Iterar sobre os dados brutos para formar as transações
    i = 0
    while i < len(dados_brutos):
        if re.match(data_regex, dados_brutos[i]):  # Verifica se o item é uma data
            data_atual = dados_brutos[i]
            i += 1
        elif dados_brutos[i]:  # Se o item não for vazio e não for uma data
            # Formar a transação e adicionar às listas
            transacao = [data_atual, dados_brutos[i], dados_brutos[i + 1], dados_brutos[i + 2]]
            transacoes.append(transacao)
            i += 3
        else:
            i += 1

    # Caminho do arquivo CSV
    caminho_csv = '/media/joao/Salmo5,13/pro/script.py/automacoes/Auditoria/Programa/mnt/data/transacoes.csv'  # Ajuste o caminho conforme necessário

    # Verificar se o diretório existe, se não, criar
    diretorio = os.path.dirname(caminho_csv)
    if not os.path.exists(diretorio) and diretorio:
        os.makedirs(diretorio)

    # Sobrescrever o arquivo a cada execução
    with open(caminho_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Data", "Descrição", "Código", "Valor"])  # Escrever o cabeçalho
        for transacao in transacoes:
            writer.writerow(transacao)  # Escrever as transações
