import redis
import requests

# Conectar ao Redis
cache = redis.StrictRedis(host='localhost', port=6379, db=0)

API_KEY = 'sua_api_key'
CIDADE = 'São Paulo'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}'

def obter_clima(cidade):
    cache_key = f'clima:{cidade}'
    
    # Verificar se o clima já está no cache
    if cache.exists(cache_key):
        print("Dados em cache!")
        return cache.get(cache_key)
    
    # Caso contrário, fazer a requisição à API
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}')
    clima = response.json()
    
    # Armazenar no cache
    cache.set(cache_key, str(clima), ex=3600)  # Expira em 1 hora
    return clima

clima = obter_clima(CIDADE)
print(clima)
