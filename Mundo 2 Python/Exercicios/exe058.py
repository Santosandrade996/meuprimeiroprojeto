#Jogos de adivinhação
from random import randint

computador = randint(0,10)
print('Sou seu computador....Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar?')
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite?'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Maior...')
        elif jogador > computador:
            print('Menor...')
            
print(f'Acertou com {palpites} tentativas...')

