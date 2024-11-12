import requests

base_url = 'http://127.0.0.1:5000'

response = requests.get(f'{base_url}/spells')
if response.status_code == 200:
    print()
else:
    print(f"Erro ao acessar feitiços: {response.status_code}")

spell_id = 1  
response = requests.get(f'{base_url}/spells/{spell_id}')
if response.status_code == 200:
    print(f"Feitiço com ID {spell_id}: {response.json()}")
else:
    print(f"Erro ao acessar feitiço {spell_id}: {response.status_code}")

while True:
    input()
    break