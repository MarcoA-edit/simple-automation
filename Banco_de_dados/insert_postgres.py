import pandas as pd
import psycopg2
from datetime import datetime

host = 'HOST'
port = 'PORTA'
database = 'BANCO'
user = 'LOGIN'
password = 'SENHA'
arquivo = 'ARQUIVO'

nome_planilha = ' '

schema = 'SCHEMA ONDE A TABELA ESTA'

tabela = 'TABELA ONDE OS DADOS SERÃO INSERIDOS'

conn = psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password
)

df = pd.read_excel(arquivo, sheet_name=nome_planilha)

cursor = conn.cursor()

# Validar se ID já existe na tabela, para não gerar dados duplicados
with open('log.txt', 'a') as log_file:
    for index, row in df.iterrows():
        id = row['']
        # Verifica se o número de ID já existe na tabela
        check_query = f'SELECT COUNT(*) FROM {schema}.{tabela} WHERE id = %s;'
        cursor.execute(check_query, (id,))
        result = cursor.fetchone()

        if result[0] == 0:
            insert_query = f'''
            INSERT INTO {schema}.{tabela} ("COLUNAS NAS QUAIS OS DADOS SERÃO INSERIDAS)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            '''
            cursor.execute(insert_query, ('COLUNAS PRESENTES NO ARQUIVO DE IMPORTAÇÃO'))

            # Criando um log de importação
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_file.write(f'{timestamp} - id: {id} inserido com sucesso.\n')
        else:
            log_file.write(f'{timestamp} - Registro com id {id} já existe. Ignorando inserção.\n')

conn.commit()
cursor.close()
conn.close()

print("Tabela e dados importados com sucesso para o banco de dados PostgreSQL.")
print("Informações também foram salvas no arquivo log.txt.")
