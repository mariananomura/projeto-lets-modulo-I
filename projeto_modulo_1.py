import json
import os.path
import sys
from unicodedata import category

def obter_dados():
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

dados = obter_dados()

def listar_categorias(dados):
    lista_categorias = []
    for dicionario in dados:
        if dicionario['categoria'] not in lista_categorias:
            lista_categorias.append(dicionario['categoria'])
    return(sorted(lista_categorias))


def listar_por_categoria(dados, categoria):
    itens_categoria = []
    for dicionario in dados:
        if dicionario['categoria'] == categoria:
            itens_categoria.append(dicionario)
    return(itens_categoria)

def produto_mais_caro(dados, categoria):
    item_mais_caro = dados[0]
    for item_dicionario in dados:
        if float(item_dicionario['preco']) > float(item_mais_caro['preco']):
            item_mais_caro = item_dicionario
    return(item_mais_caro)


def produto_mais_barato(dados, categoria):
    item_mais_barato = dados[0]
    for item_dicionario in dados:
        if float(item_dicionario['preco']) < float(item_mais_barato['preco']):
            item_mais_barato = item_dicionario
    return(item_mais_barato)


def top_10_caros(dados):
    lista_10_mais_caros = sorted(dados, key=lambda valor: float(valor['preco']), reverse=True) 
    return lista_10_mais_caros[:10]
    

def top_10_baratos(dados):
    lista_10_mais_baratos = sorted(dados, key=lambda valor: float(valor['preco'])) 
    return lista_10_mais_baratos[:10]

def selecionar_categoria():
    lista_categorias= listar_categorias(dados)
    categoria = input('Digite a categoria desejada: ')
    while categoria not in lista_categorias:
        print('categoria inválida!')
        categoria = input('Digite a categoria desejada: ')
    else:
        return categoria

def imprimir_lista(lista):
    for item in lista:
        print(f'- {item}\n')


def menu(dados):
    print('Seja bem-vindo(a) ao portal de produtos!\nEscolha uma das opções para continuar:')
    
    escolha_usuario = -1

    while escolha_usuario !=0:

        print(
        '1. Listar categorias\n'
        '2. Listar produtos de uma categoria\n'
        '3. Produto mais caro por categoria\n'
        '4. Produto mais barato por categoria\n'
        '5. Top 10 produtos mais caros\n'
        '6. Top 10 produtos mais baratos\n'
        '0. Sair')

        escolha_usuario=int(input('Digite o número da opção desejada: '))

        if escolha_usuario==1:
            lista = listar_categorias(dados)
            imprimir_lista(lista)

        elif escolha_usuario==2:
            categoria = selecionar_categoria()
            lista= listar_categorias(categoria)
            print(f'Produtos disponíveis na categoria {categoria}:\n')
            imprimir_lista(lista)

        elif escolha_usuario==3:
            categoria = selecionar_categoria()
            mais_caro = produto_mais_caro(dados, categoria)
            print(f'Produto mais caro da categoria {categoria}:\n {mais_caro}')

        elif escolha_usuario==4:
            categoria = selecionar_categoria()
            mais_barato = produto_mais_barato(dados, categoria)
            print(f'Produto mais barato da categoria {categoria}:\n {mais_barato}')

        elif escolha_usuario==5:
            lista = top_10_caros(dados)
            print(f'Top 10 produtos mais caros:\n')
            imprimir_lista(lista)

        elif escolha_usuario==6:
            lista = top_10_baratos(dados)
            print(f'Top 10 produtos mais baratos:\n')
            imprimir_lista(lista)

        elif escolha_usuario==0:
            print('Sessão encerrada!\nAté mais!')
            break
        else:
            print('Opção inválida!')
            
# Programa Principal - não modificar!
dados = obter_dados()
menu(dados)