from random import choice

n1 = str(input('Digite o primeiro nome do aluno: '))
n2 = str(input('Digite o segundo nome do aluno: '))
n3 = str(input('Digite o terceiro nome do aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}' .format(escolhido))
# Sorteando um item na lista.



