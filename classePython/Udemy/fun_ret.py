"""

print('####### Funções de Retorno #######')

numeros = [1, 2, 3]

#numeros.pop() #remove o ultimo numero da lista
ret_pop = numeros.pop()

print(f' Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f' Retorno de pop: {ret_pop}')

print(numeros)

def quadrad_de_7():
    return 7 * 7

ret = quadrad_de_7()
print(f'Retorno : {ret}')

print(f'Retorno : {quadrad_de_7()}')

from random import random


def joga_moeda():

    valor = random()
    if valor >0.5:
        return 'Cara 💿'
    return 'Coroa 📀'

print(joga_moeda())

#seis linha para iniciar os comentarios

"""

print(f'####### Funções de Retorno #######')

