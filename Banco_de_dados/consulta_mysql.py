import mysql.connector
import pandas as pd

conexao_bd = mysql.connector.connect(
    host='HOST DO BANCO',
    user='LOGIN',
    password='SENHA',
    database='BASE A SER CONSULTADA'
)

consulta_sql = """
CONSULTA
"""

cursor = conexao_bd.cursor()

resultados = cursor.fetchall()

colunas = [i[0] for i in cursor.description]

cursor.close()
conexao_bd.close()

if resultados:
    resultado_df = pd.DataFrame(resultados, columns=colunas)

    resultado_df.to_excel('.xlsx', index=False)
else:
    print("Erro")
