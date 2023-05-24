#pow serve para potencia, numero**(1/2) raiz cubica.
#DEsafio. FAça um programa que exiba seu antecesso e sucessor

print('='*15)
r1 = int(input('Digite um numero:'))
r2 = int(input('Digite um numero:'))

sa = r1+r2
mm = r1 * r2
dv = r1 / r2
ex = r1 // r2
mo = r1 ** r2

print('Os resultados deste calculo é {} e a divisão é {:.3f}'.format(sa, mm, dv), end=' ')
print('Divisão inteira {} e Potência {}'.format(dv, mo))