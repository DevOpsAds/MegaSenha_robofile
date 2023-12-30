import re
import csv
import os

# Dados brutos fornecidos
dados_brutos = [
    "12/09", "12/09", "12/09", "12/09", "12/09", "12/09", "", 
    "MOBILEPAG TIT 4800148270", "2.96217.1 9427", "1.783,06-",
    "PIX TRANSF ANA LUC", "32.61209.1 9136", "3.500,00-",
    "PIX TRANSF ANA LUC", "32.98933.1 9126", "3.500,00-",
    "EST PIX TF ANA LUCIA", "76.12029.1 9026", "3.500,00",
    "EST PIX TE ANA LUCIA", "76.75359.1 9122", "3.500,00",
    "RES APLIC AUT MAIS", "74.09117.8", "10.788,27",
    "REND PAGO APLIC AUT MAIS", "74.09117.8", "0,03"
]

# Inicializar listas vazias para datas, descrições, códigos e valores
datas = []
descricoes = []
codigos = []
valores = []

# Regex para identificar as datas
data_regex = r"\d{2}/\d{2}"

# Variável para manter a data atual
data_atual = ""

# Iterar sobre os dados brutos
for item in dados_brutos:
    if re.match(data_regex, item):  # Verifica se o item é uma data
        data_atual = item
    elif item:  # Se o item não for vazio e não for uma data
        datas.append(data_atual)
        descricoes.append(item)
        codigos.append("")  # Adicionar espaço vazio por enquanto
        valores.append("")  # Adicionar espaço vazio por enquanto

# Atribuir os códigos e valores às transações
indice_transacao = 0
for i in range(len(dados_brutos)):
    if dados_brutos[i] in descricoes:
        codigos[indice_transacao] = dados_brutos[i + 1] if i + 1 < len(dados_brutos) else ""
        valores[indice_transacao] = dados_brutos[i + 2] if i + 2 < len(dados_brutos) else ""
        indice_transacao += 1

# Caminho do arquivo CSV
caminho_csv = '/media/joao/Salmo5,13/pro/script.py/automacoes/Auditoria/Programa/mnt/data/transacoes.csv'

# Verificar se o arquivo já existe
diretorio = os.path.dirname(caminho_csv)
if not os.path.exists(diretorio):
    os.makedirs(diretorio)

existe_arquivo = os.path.exists(caminho_csv)
with open(caminho_csv, mode='a' if existe_arquivo else 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Se o arquivo não existir, escrever o cabeçalho
    if not existe_arquivo:
        writer.writerow(["Data", "Descrição", "Código", "Valor"])
    
    # Escrever os dados
    for data, descricao, codigo, valor in zip(datas, descricoes, codigos, valores):
        writer.writerow([data, descricao, codigo, valor])



