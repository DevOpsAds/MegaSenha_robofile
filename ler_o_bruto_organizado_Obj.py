import pandas as pd



def tratamento_dados_brutos_organizado_white_pag(dados_processados):
    # Dados processados fornecidos como uma lista de dicionários
 
    print("OBJETO",dados_processados)
    # Caminho do arquivo CSV
    caminho_csv = '/media/joao/Salmo5,13/pro/script.py/automacoes/Auditoria/Programa/mnt/data/transacoes.csv'  # Ajuste o caminho conforme necessário

    # Carregar os dados existentes se o arquivo já existir, caso contrário, criar um DataFrame vazio
    try:
        dados_existentes = pd.read_csv(caminho_csv)
    except FileNotFoundError:
        dados_existentes = pd.DataFrame(columns=['Data', 'Descrição', 'Código', 'Valor'])

    # Convertendo os dados processados em um DataFrame
    novo_df = pd.DataFrame(dados_processados)

    # Concatenar com os dados existentes
    dados_concatenados = pd.concat([dados_existentes, novo_df], ignore_index=True)

    # Salvar no arquivo CSV
    dados_concatenados.to_csv(caminho_csv, index=False)

    caminho_csv

    print("outra imagem muito bem!")

