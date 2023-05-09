# Jogo de advinhação...
from random import randint
from time import sleep

computador = randint(0, 5)  # Faz o computador 'PENSAR'
print('-=-' * 24)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
print('-=-' * 24)
jogador = int(input('Em que número eu pensei? '))  # O jogador tenta 'ADIVINHAR'
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS você conseguiu me vencer! ')
else:
    print('GANHEI! eu pensei no número {} e não no {} !'.format(computador, jogador))


