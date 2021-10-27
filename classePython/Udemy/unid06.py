"""
Estrutura de repetição
sendo o for para exibir essa repetição;

"""
#variavel
nome = 'Geek University - Criando Possibilidades'
Lista = [1,2,3,4,5,6,7]
num = range(1, 16)

#executando o programa

"""
print('----#### Usando o Loop e o For ####----')
for letra in nome:
    print(letra)

for numero in Lista:
    print(numero)

for numero in range(1,16):
    print(numero)

#serve para gerar uma tupla dentro do vetor
for i, v in enumerate(nome):
    print(nome[i])

qnt = int(input('Quantas vezes esse Loop deve rodar?: '))

for n in range(1, qnt):
    print(f'Imprimindo {n}')

qnt = int(input('Quantas vezes esse Loop deve rodar?: '))
soma = 0

for n in range(1, qnt+1):
    num = int(input(f' Informe o {n}/{qtd} valor: '))
    soma = soma + num
    print(f'A soma é {soma}')
"""
qnt = int(input('Quantas vezes esse Loop deve rodar?: '))
soma = 0

for n in range(1, qnt+1):
    
    num = int(input(f' Informe o {n}/{qnt} valor: '))
    soma = soma + num
print(f'A soma é {soma}')
    
#fim do programa