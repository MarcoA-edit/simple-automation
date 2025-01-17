import psycopg2
import pandas as pd

db_params = {
    'host': 'HOST DO BANCO',
    'port': 0000,
    'user': 'LOGIN',
    'password': 'SENHA',
    'database': 'BASE A SER CONSULTADA'
}

query = """
CONSULTA;
"""

try:
    connection = psycopg2.connect(**db_params)
    df = pd.read_sql_query(query, connection)
finally:
    connection.close()

output_file = ".xlsx"
df.to_excel(output_file, index=False)