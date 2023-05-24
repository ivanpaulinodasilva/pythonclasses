#Trabalhando com módulos e pacotes,
# import, traz a libary em python.  sendo que from 'tipo' import 'tipoimport' traz uma 
#classificação dentro desta libary. import, math;ceil,floor,trunc,pow,sqrt,factorial
#import math or from 'math' import 'sqrt' importa (somente sqrt)
#bebida: comida: doce:

#prática
import math


num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

#Desafio
#016 Escreva um programa real que ao ser digitado apareça em tela sua porção inteira;
#017 Leia a hipotenusa de um cateto oposto e seu adjacente;
#018 Ao receber um ângulo, defina seu sen, cos, tag;
#019 Faça um sorteio que ao receber o nome dos quatros alunos deve aparecer somente um nome;
#020 Faça um sorteio que ao receber o nome dos quatros alunos deve aparecer a ordem de sorteio
# dos quatro alunos;   
#021 Faça um programa que abra e reproduta um arquivo de audio-mp3.