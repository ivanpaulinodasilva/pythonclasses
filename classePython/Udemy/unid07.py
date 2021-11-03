"""
Listas e Bibliotecas python

num = 8

if num in lista4:
    print(f'Encontrei o número {num} ')
else:
    print(f'Não encontrei o número {num} ')

lista1.sort()
print(f'{lista1}')

#serve para pesquisar a contagem de números ou exibir letras
print(lista1.count(1))
print(lista5.count('i'))

#serve para inserir valores e fazer uma nova contagem
print(lista1)
lista1.append(42)
print(lista1)

#pesquisa lista e acresenta quando necessario.
lista1.append([8,3,11])
print(lista1)

if[8,3,11] in lista1:
    print('Encontrei a Lista !')
else:
    print('Não encontrei a lista, veja novamente! ')

lista1.append([8,3,11]) #adiciona como objeto único.
print(lista1)

lista1.extend([123,44,67]) #coloca itens dentro da lista adicional

if[8,3,11] in lista1:
    print('Encontrei a Lista !')
else:
    print('Não encontrei a lista, veja novamente! ')

lista1.reverse() #usado para ordenar lista

#slice
print(lista1[::-1])

lista1.copy() #cria uma lista simples em cópia

print(len(lista2)) #contar os elemento de lista

print(lista1)
lista1.pop() #remove o ultimo elemento de uma lista e retorna quando solicitado.
print(lista1)

lista1.clear #limpa uma lista para ser inserida novamente

nome da lista * 3 #repeti elemento em lista, em uma lista criada!

nome da lista.split() #separa os elementos dentro de uma string

#Exemplo de Lista
carrinho = []
produto = ''

while produto != ('sair'):
    print("Adicione um produto na lista ou digite 'sair' para finalizar a compra. ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

#Revisão slicing, [inicio fim e passo]

listasg = [1,2,3,4] #lista com slicing recebendo esse título

print(listasg[1:])#eliminando o inicio e dando o fim e passo

 
"""

print('#### Criando listas e Bibliotecas ####')

type([])

lista1 = [1,99,4,27,15,22,3,1,44,42,71]

lista2 = ['I','V','A','N','','S','I','L','V','A']

lista3 = []

lista4 = list(range(11))

lista5 = list('SkyNET Construindo o Futuro')

#Exemplo de Lista com variaveis

#copiando uma lista para outra, em entrevista de emprego

listacp = [1,2,3,4]

print(listacp)

nlistacp = listacp.copy()

print(nlistacp)

nlistacp.append(7)  #são lista diferentes a cada inerção

print(listacp)
print(nlistacp)     #são listas independentes e formato e elementos, chamando de "deep copy"

#shallow copy

nslista = [5,7,9,11]

print(nslista)

nsnlista = (nslista)

nsnlista.append(13)

print(nsnlista)