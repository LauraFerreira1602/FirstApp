# Criar lista com 5 objetos
objetos = ["cadeira", "mesa", "prato", "copos", "talheres"]
print('Lista criada com sucesso.')

# Adicionar objeto a lista
objetos.append('jarra')
print('jarra adicionada a lista')

# Acessar item da lista
acesso = objetos[2]
print('O item acessado é:', objetos[2])

# Remover item da lista
objetos.remove('jarra')
print('jarra removida da lista')

# Tamanho da lista
print('Quantidade de items na lista:')
len(objetos)
print(len(objetos))

# Mostrar todos os items da lista
print('Items existentes na lista:')
for item in objetos:
    print(item)

# Verificar e remover um item existente da lista
objetos.pop(0)
print('Cadeira removida da lista')

# Ordene a lista em ordem alfabética
objetos.sort()
print('Lista ordenada em ordem alfabetica:', objetos)

# Exibir o primeiro e o último objeto
objeto_1 = objetos[1]
objeto_ultimo = objetos[len(objetos) - 1]
print('Primeiro e ultimo item da lista :', objeto_1, objeto_ultimo)

# Limpar toda a lista
objetos.clear()
print('Os items desta lista foram apagados.')