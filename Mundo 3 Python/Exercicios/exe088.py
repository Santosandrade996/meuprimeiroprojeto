#Correção/ Sorteio do mega-sena

from random import randint
from time import sleep

lista = list()
jogos = list()
print('-=' * 30)
print('                 Sorteio Mega Sena        ')
print('-=' * 30)

quant = int(input('Quantos jogos se quer que eu sorteie? '))
tot = 0
while tot < quant:
    cont = 0
    num = randint(1,60)

    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'-=' * 3 , f'Sorteando {quant} Jogos!', '-=' * 3)
for i, l in enumerate(jogos):
    print(f' Jogo {i+1}: {l}')
    sleep(1)
    
print('-=' * 5, '< Boa Sorte! >', '-=' * 5)

