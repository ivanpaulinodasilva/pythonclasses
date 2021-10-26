"""
condicionais estruturas lógicas
if teste de conparação de uma variavel ou outra

"""
idade = 18

print("####---->Estruturas Condicionais<----####")
print("Apresente as seguintes idades: Bebê, Criança, Adolescente, Adulto e Idoso")

if idade < 18:
    print('Menor de Idade')
elif idade == 18:
    print('está com 18 anos')
else:
    print('Maior de Idade')
