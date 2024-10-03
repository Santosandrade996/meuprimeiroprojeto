#Refazendo o exercicios 028 com a utilização while
from random import randint
from time import sleep

computador = randint(0, 10)

print('=' * 25)
print('O Computador pensou em um número entre 0 e 10 tente advinhar...')
print('=' * 25)

jogador = int(input('Em que número pensei?'))
print('PROCESSANDO...')
sleep(4)

tentativas = 0

while True:
    jogador = int(input('Digite seu palpite:'))
    tentativas += 1
    
    if jogador == computador:
        print(f'Parabens Você acertou o número secreto é {jogador, computador}! ....')
        
        break
    elif jogador < computador:
        print('Tente um número maior!')
    else:
        print('Tente um número menor!')
