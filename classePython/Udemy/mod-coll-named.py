"""
Módulo de named tuple

dog =  namedtuple('cachorro', 'idade raca nome')

dog =  namedtuple('cachorro', 'idade, raca, nome')

dog =  namedtuple('cachorro', ['idade', 'raca', 'nome'])

ray = dog(idade=2, raca='cheetos', nome='ray')

print(ray)

#forma de exibição -1

print(ray[0])
print(ray[1])
print(ray[2])

#forma de exibição -2

print(ray.idade)
print(ray.nome)
print(ray.raca)

"""
from collections import namedtuple

dog =  namedtuple('cachorro', 'idade raca nome')

dog =  namedtuple('cachorro', 'idade, raca, nome')

dog =  namedtuple('cachorro', ['idade', 'raca', 'nome'])

ray = dog(idade=2, raca='cheetos', nome='ray')

print(ray)


#forma de exibição -2

print(ray.idade)
print(ray.nome)
print(ray.raca)

