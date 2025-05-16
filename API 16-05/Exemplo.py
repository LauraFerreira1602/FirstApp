import requests

cep = "01001000"
url = f"https://viacep.com.br/ws/{cep}/json/"
response = requests.get(url)

if response.status_code == 200:
    dados_cep = response.json()
    print(f' Região: {dados_cep["regiao"]}')
    print(f' Cidade: {dados_cep["localidade"]}')
    print(f' Bairro: {dados_cep["bairro"]}')
    print(f' Rua: {dados_cep["logradouro"]}')

else:
    print(f' Erro: {response.status_code}')