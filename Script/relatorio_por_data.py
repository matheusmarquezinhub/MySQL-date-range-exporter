# Importações necessárias: datetime para manipulação de datas, mysql.connector para conexão com MySQL, e csv para geração de arquivos CSV.
from datetime import datetime
import mysql.connector
import csv

# Estabelece a conexão com o banco de dados MySQL.
conexao = mysql.connector.connect(
    host="localhost",          # Endereço do servidor MySQL (geralmente localhost para desenvolvimento local).
    user="root",               # Usuário do banco de dados.
    password="",               # Senha do banco (deixe vazio se não houver senha).
    database=""                # Nome do banco de dados a ser usado.
)

# Cria um cursor para executar consultas SQL.
cursor = conexao.cursor()

# Função para obter e validar uma data inserida pelo usuário no formato DD-MM-YYYY.
def obter_data(mensagem):
    while True:
        try:
            data_str = input(mensagem)  # Solicita entrada do usuário.
            data_obj = datetime.strptime(data_str, "%d-%m-%Y")  # Converte string para objeto datetime.
            return data_obj.date()  # Retorna apenas a parte da data (sem hora).
        except ValueError:
            print("Formato inválido! Use DD-MM-YYYY")  # Mensagem de erro se o formato estiver errado.

# Solicita ao usuário as duas datas para o intervalo de consulta.
data1 = obter_data("Digite a primeira data (DD-MM-YYYY): ")
data2 = obter_data("Digite a segunda data (DD-MM-YYYY): ")

# Define a consulta SQL para selecionar registros da tabela onde a coluna 'Data' está entre as datas fornecidas, ordenados por data decrescente.
# IMPORTANTE: Substitua 'tabela' pelo nome real da sua tabela e ajuste a consulta conforme necessário.
query = "SELECT * FROM tabela WHERE Data BETWEEN %s AND %s ORDER BY Data DESC"

# Executa a consulta SQL, passando as datas como parâmetros para evitar injeção de SQL.
cursor.execute(query, (data1, data2))

# Obtém os nomes das colunas do resultado da consulta (para usar como cabeçalho no CSV).
colunas = [desc[0] for desc in cursor.description]

# Obtém todos os registros retornados pela consulta.
resultados = cursor.fetchall()

# Gera um nome dinâmico para o arquivo CSV, incluindo as datas do intervalo.
nome_arquivo = f"relatorio_{data1}_ate_{data2}.csv"

# Cria e escreve o arquivo CSV com os dados.
with open(nome_arquivo, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')  # Usa ';' como delimitador (comum em regiões que usam vírgula como separador decimal).
    
    # Escreve a linha de cabeçalho com os nomes das colunas.
    writer.writerow(colunas)
    
    # Escreve cada linha de dados no CSV.
    for linha in resultados:
        writer.writerow(linha)

# Exibe mensagens de confirmação no console.
print(f"\n✓ Arquivo '{nome_arquivo}' gerado com sucesso!")
print(f"✓ Total de registros: {len(resultados)}")

# Fecha o cursor e a conexão com o banco para liberar recursos.
cursor.close()
conexao.close()
