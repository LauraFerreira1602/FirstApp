from urllib import response

import requests

def exemplo_cep():
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


def exemplo_get(id):
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"
    response = requests.get(url)

    if response.status_code == 200:
        dados_get_postagem = response.json()

        print(f"Titulo: {dados_get_postagem['title']}\n")
        print(f"Conteudo: {dados_get_postagem['body']}")

    else:
        print(f' Erro: {response.status_code}')


def exemplo_post():
    url = " https://jsonplaceholder.typicode.com/posts"

    nova_postagem = {
        "title": "Postagem",
        "body": "Novo conteudo",
        "userId": 1
    }

    response = requests.post(url, json=nova_postagem)

    if response.status_code == 201:
        dados_postagem = response.json()
        print(f"Titulo: {dados_postagem['title']}\n")
        print(f"Conteudo: {dados_postagem['body']}")

    else:
        print(f"Erro: {response.status_code}")


def exemplo_put():
    url = f"https://jsonplaceholder.typicode.com/posts/1"
    response = requests.put(url)

    if response.status_code == 200:
        dados_put = response.json()

        print(f"Titulo: {dados_put['title']}\n")
        print(f"Conteudo: {dados_put['body']}")

    else:
        print(f' Erro: {response.status_code}')


# exemplo_get(50)
exemplo_post()