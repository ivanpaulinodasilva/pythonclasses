"""
container datetypes

Couter -  recebe como inteiro e retorna como objeto. 
from collections import Counter


lista =  [1,1,1,2,2,2,3,3,3,33,1,11,11,1,1,1,5,5,5,5,5,5,3,45,45,45,45,66,66,66,43,34]


res = Counter(lista)
print(res)

texto = ""O Lorem Ipsum é um texto modelo da indústria tipográfica e de impressão. 
O Lorem Ipsum tem vindo a ser o texto padrão usado por estas indústrias desde o ano de 1500, 
quando uma misturou os caracteres de um texto para criar um espécime de livro. 
Este texto não só sobreviveu 5 séculos, mas também o salto para a tipografia electrónica, 
mantendo-se essencialmente inalterada. Foi popularizada nos anos 60 com a disponibilização
das folhas de Letraset, que continham passagens com Lorem Ipsum, e mais recentemente 
com os programas de publicação como o Aldus PageMaker que incluem versões do Lorem Ipsum.""

palavras =texto.split()

res = Counter(palavras)

print(res)
"""
from collections import Counter

