import json
import os.path
import sys
from unicodedata import category


def obter_dados():
    '''Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.'''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados


dados = obter_dados()


def listar_categorias(dados:list) -> list:
    '''Retorna uma lista contendo todas as categorias dos diferentes produtos.'''
    lista_categorias = []
    for dicionario in dados:
        if dicionario['categoria'] not in lista_categorias:
            lista_categorias.append(dicionario['categoria'])
    return sorted(lista_categorias)


def listar_por_categoria(dados: list, categoria: str) -> list:
    '''Retorna uma lista contendo todos os produtos pertencentes à categoria dada.'''
    itens_categoria = []
    for dicionario in dados:
        if dicionario['categoria'] == categoria:
            itens_categoria.append(dicionario)
    return itens_categoria


def produto_mais_caro(dados: list, categoria: str) -> dict:
    '''Retorna um dicionário representando o produto mais caro da categoria dada.'''
    itens_categoria = listar_por_categoria(dados, categoria)
    item_mais_caro = itens_categoria[0]
    for item in itens_categoria:
        if float(item['preco']) > float(item_mais_caro['preco']):
            item_mais_caro = item
            return item_mais_caro


def produto_mais_barato(dados: list, categoria: str) -> dict:
    '''Retorna um dicionário representando o produto mais barato da categoria dada.'''
    itens_categoria = listar_por_categoria(dados, categoria)
    item_mais_barato = itens_categoria[0]
    for item_dicionario in itens_categoria:
        if float(item_dicionario['preco']) < float(item_mais_barato['preco']):
            item_mais_barato = item_dicionario
    return item_mais_barato


def top_10_caros(dados: list) -> list:
    '''Retorna uma lista de dicionários representando os 10 produtos mais caros.'''
    lista_10_mais_caros = sorted(
        dados, key=lambda valor: float(valor['preco']), reverse=True)
    return lista_10_mais_caros[:10]


def top_10_baratos(dados: list):
    '''Retorna uma lista de dicionários representando os 10 produtos mais baratos.'''
    lista_10_mais_baratos = sorted(
        dados, key=lambda valor: float(valor['preco']))
    return lista_10_mais_baratos[:10]


def selecionar_categoria() -> str:
    '''Recebe o input do usuário e converte para minúsculo para validação. Retorna a categoria. '''
    lista_categorias = listar_categorias(dados)
    categoria = input('Digite a categoria desejada: ').lower()
    validar_categoria(categoria, lista_categorias)
    return categoria
    

def validar_categoria(categoria: str, lista: list): 
    '''Valida a categoria. Dá a opção de retornar ao menu principal no caso de categorias inválidas ou retorna a categoria validada.'''
    while categoria not in lista:
        print('\nCategoria inválida!')
        categoria = input('Digite a categoria desejada ou digite 0 para retornar ao menu: ').lower()
        if categoria == '0':
            menu(dados)
    else:
        return categoria


def imprimir_lista(lista: list) -> None: 
    '''Formata a resposta para o usuário quando a resposta inclui mais de um item.'''  
    for item in lista:
        if type(item) == dict:
            print(f'ID:{item["id"]}\nPreço: {item["preco"]}\nCategoria: {item["categoria"]}\n')
        else:
            print(f'-{item}')


def imprimir_item_unico(item: dict) -> None:
    '''Formata a resposta para o usuário quando a resposta inclui somente um item.'''
    print(f'ID: {item["id"]}\nPreço: {item["preco"]}\nCategoria: {item["categoria"]}\n')


def menu(dados: list) -> None:
    '''Em loop, exibe um menu de opções para o usuário, lê o input do usuário e chama a função adequada para tratar o pedido do usuário.'''
    print('Seja bem-vindo(a) ao portal de produtos!\nEscolha uma das opções para continuar:')

    escolha_usuario = -1

    while escolha_usuario != 0:

        print(
            '1. Listar categorias\n'
            '2. Listar produtos de uma categoria\n'
            '3. Produto mais caro por categoria\n'
            '4. Produto mais barato por categoria\n'
            '5. Top 10 produtos mais caros\n'
            '6. Top 10 produtos mais baratos\n'
            '0. Sair')

        escolha_usuario = (input('Digite o número da opção desejada: '))

        if escolha_usuario == '1':
            lista = listar_categorias(dados)
            imprimir_lista(lista)

        elif escolha_usuario == '2':
            categoria = selecionar_categoria()
            lista = listar_por_categoria(dados, categoria)
            print(f'\nProdutos disponíveis na categoria {categoria}:\n')
            imprimir_lista(lista)

        elif escolha_usuario == '3':
            categoria = selecionar_categoria()
            mais_caro = produto_mais_caro(dados, categoria)
            print(f'\nProduto mais caro da categoria {categoria}:')
            imprimir_item_unico(mais_caro)

        elif escolha_usuario == '4':
            categoria = selecionar_categoria()
            mais_barato = produto_mais_barato(dados, categoria)
            print(f'\nProduto mais barato da categoria {categoria}:')
            imprimir_item_unico(mais_barato)

        elif escolha_usuario == '5':
            lista = top_10_caros(dados)
            print(f'\nTop 10 produtos mais caros:\n')
            imprimir_lista(lista)

        elif escolha_usuario == '6':
            lista = top_10_baratos(dados)
            print(f'\nTop 10 produtos mais baratos:\n')
            imprimir_lista(lista)

        elif escolha_usuario == '0':
            print('\nSessão encerrada!\nAté mais!')
            break
        else:
            print('\nOpção inválida!\n')


# Programa Principal
dados = obter_dados()
menu(dados)
