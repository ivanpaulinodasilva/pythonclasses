### Normalmente, a matemática envolve cerca de quatro operações principais: adição, subtração, 
### multiplicação e divisão. O Python dá suporte a essas quatro operações e a algumas outras. 
### Vamos explorar as operações mais comuns que você usará em seus programas.

# Adição
###answer = 30 + 12
###print(answer)

# Subtração
###difference = 30 - 12
###print(difference)

# Multiplicação
###product = 30 * 12
###print(product)

# Divisão
###quotient = 30 / 12
###print(quotient)

#Trabalhando com Modulo e Divisão
###seconds = 1042
###display_minutes = 1042 // 60
###display_seconds = 1042 % 60

###print(display_minutes)
###print(display_seconds)


#Display distance between planets

###first_planet = 149597870
###second_planet = 778547200

###distance_km = second_planet - first_planet
###print(distance_km)

###distance_mi = distance_km / 1.609344
###print(distance_mi)

#Convertendo tipos de dados
###demo_int = int('215')
###print(demo_int)

###demo_float = float('215.3')
###print(demo_float)


#Importanto bibliotecas Matemática

###from math import ceil, floor

###round_up = ceil(12.5)
###print(round_up)

###round_down = floor(12.5)
###print(round_down)

### Exercício converter cadeias de caracteres em números e usar valores absolutos

first_planet_input = input('Enter the distance from the sun for the first planet in km')
second_planet_input = input('Enter the distance from the sun for the second planet in km')

first_planet = int(first_planet_input)
second_planet = int(second_planet_input)

distance_km = second_planet - first_planet
print(abs(distance_km)+'Essa é atual distancia entre os planetas. ')