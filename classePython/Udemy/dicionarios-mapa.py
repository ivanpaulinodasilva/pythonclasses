"""
Mapa

dicionario são relacionado como Chave/Valor.

dicionario são representados por chaves {}.

print(type({}))

print('#### Dicionario - Mapa ####')

paises = {'br': 'Brasil','eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

pais = paises.get('ru', 'Não encontrado')

if pais:
    print(f'Encontrei o pais{paises}')

else:
    print('Não encontrado o Pais')


    print('#### Dicionario - Mapa ####')

paises = {'br': 'Brasil','eua': 'Estados Unidos', 'py': 'Paraguai'}

# adicionar elementos em dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

#Add forma 01 <- Mais comum

receita['abr'] = 300
print(receita)

#Add forma 02

novo_dado={'mai': 500}
receita.update(novo_dado)
print(receita)

#forma 01 de remover do dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

receita.pop('mar')
print(receita)

#forma 02

del receita['fev']
print(receita)

"""

#forma 01 de remover do dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

receita.pop('mar')
print(receita)

#forma 02

del receita['fev']
print(receita)