import mysql.connector as _mysql_connector
import requests

API_KEY = 'sua_api_key'
CIDADE = 'São Paulo'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}'

# Conectar ao banco de dados (se não existir, será criado)
conn = _mysql_connector.connect('clima.db')
cursor = conn.cursor()

# Criar a tabela de clima
cursor.execute('''
CREATE TABLE IF NOT EXISTS clima (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cidade TEXT,
    temperatura REAL,
    descricao TEXT,
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Obter dados da API
response = requests.get(URL)
data = response.json()

if response.status_code == 200:
    temperatura = data['main']['temp']
    descricao = data['weather'][0]['description']
    
    # Armazenar os dados no banco
    cursor.execute('''
    INSERT INTO clima (cidade, temperatura, descricao)
    VALUES (?, ?, ?)
    ''', (CIDADE, temperatura, descricao))
    conn.commit()
    print("Dados armazenados com sucesso!")
else:
    print("Erro ao obter dados:", data)

conn.close()
