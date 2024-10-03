# Pedra papel e tesoura

from random import randint
from time import sleep

itens = ['Pedra', 'Papel' , 'Tesoura']
computador = randint(0, 2)
print('''Sua opções...
      [0] Pedra
      [1] Papel
      [2] Tesoura''')

jogador = int(input('Qual é a sua jogada?'))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=' *12)

print('Computador jogou {}' .format(itens [computador]))
print('O jogador jogou {}' .format(itens [jogador]))

print('-=' *12)

if computador == 0: #Computador escolheu ''PEDRA''
   
    if jogador == 0:
        print('Empate')
        
    elif jogador == 1: 
        print('Jogador Vence!')
            
    elif jogador == 2: 
        print('Computador Vence!')
    else:
        print('Opção Invalida!')
        
elif computador == 1: #Computador jogou '''PAPEL'''
    
    if jogador == 0:
        print('Computador Vence!')
    
    elif jogador == 1:
        print('Empate')
    
    elif jogador == 2:
        print('Jogador Vence!')
    
    else:
        print('Opção Invalida!')

elif computador == 2: #Computador escolheu ''TESOURA''
    
    if jogador == 0:
        print('Jogador Vence!')
    
    elif jogador == 1:
        print('Computador Vence!')
    
    elif jogador == 2:
        print('Empate')
    
    else:
        print('Opção Invalida!')
        
        
        

        
        