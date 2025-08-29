from urllib import response

import requests

def exemplo_cep(cep):
    # cep = "01001000"
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    return response.json()

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
    url = "https://jsonplaceholder.typicode.com/posts"

    nova_postagem = {
        "title": "Novo titulo",
        "body": "Novo conteudo",
        "userId": 1
    }

    response = requests.post(url, json=nova_postagem)

    if response.status_code == 201:
        dados_postagem = response.json()
        print(f"Titulo: {dados_postagem['title']}")
        print(f"Conteudo: {dados_postagem['body']}")

    else:
        print(f"Erro: {response.status_code}")


def exemplo_put(id):
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"

    nova_postagem = {
        "id": id,
        "title": "Novo titulo",
        "body": "Novo conteudo",
        "userId": 1
    }

    antes = requests.get(url)
    response = requests.put(url, json=nova_postagem)

    if response.status_code == 200:
        if antes.status_code == 200:
            dados_antes = antes.json()
            print(f'Titulo Antigo: {dados_antes["title"]}')
        else:
            print(f' Erro: {response.status_code}')
        dados_postagem = response.json()
        print(f"Titulo: {dados_postagem['title']}")

    else:
        print(f"Erro: {response.status_code}")

# exemplo_get(50)
# exemplo_post()
exemplo_put(70)