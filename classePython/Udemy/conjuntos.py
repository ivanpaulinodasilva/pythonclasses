"""
Conjuntos, Teoria dos Conjuntos na Matématica.

- em python são chamados em SET'S. não possuel duplicados ou ordenados.

lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print (f 'Lista: {lista}')

tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f 'Tupla: {tupla}')

dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34]) 
print(f'Dicionario: {dicionario}')

conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34} 
print(f'Conjuntos {conjunto}')

s =  {1, 'b', True, 34, 21, 44}
print(s)
print(type(s))

for valor in s :
    print(valor)

# aplicações do uso do set

cidades =  ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiabá', 'Campo Grande', 'São Paulo', 'Cuiabá']
print(cidades)
print(len(cidades))

print(len(set(cidades)))    

unicos1 = estudantes_python.union(estudantes_java)
{'Pedro', 'Fernando', 'Ana', 'Julia', 'Guilherme', 'Patricia', 'Marcos', 'Ellen', 'Gustavo'}

unicos1 = estudantes_java.union(estudantes_python)
{'Sergio', 'Flavio', 'Mara', 'Juliana', 'Gabriel', 'Priscila', 'Mauricio', 'Hellen', 'Gusmão'}

unicos2 = estudantes_python | estudantes_java
print(unicos2)
"""
estudantes_python = {'Pedro', 'Fernando', 'Ana', 'Julia', 'Guilherme', 'Patricia', 'Marcos', 'Ellen', 'Gustavo'}

estudantes_java = {'Sergio', 'Flavio', 'Mara', 'Juliana', 'Gabriel', 'Priscila', 'Mauricio', 'Hellen', 'Gusmão'}

unicos2 = estudantes_python | estudantes_java
print(unicos2)

