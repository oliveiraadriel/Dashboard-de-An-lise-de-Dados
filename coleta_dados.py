import requests

API_KEY = 'sua_api_key'  # Substitua por sua chave de API do OpenWeatherMap
CIDADE = 'São Paulo'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}'

response = requests.get(URL)
data = response.json()

if response.status_code == 200:
    print(f"Clima de {CIDADE}:")
    print(f"Temperatura: {data['main']['temp']}°K")
    print(f"Descrição: {data['weather'][0]['description']}")
else:
    print("Erro ao obter dados:", data)
