#Par ou Impar
from random import random

print('-=' *11)
print('Jogo de Par ou Ímpar')
print('-=' * 11)

contador = 0

while True:
    jogador_num = int(input('Digite um valor:'))
    jogador_esc = input('Escola se quer Par ou Ímpar? [P/I]:').strip().upper()
    
    while jogador_esc not in('P' , 'I'):
        jogador_esc = input('Escolha Ínvalida! Escolha Porfavor se for Par ou Ímpar? [P/I]:').strip().upper()
        
        computador_num2 = random.randint(0,10)
        total = jogador_num + computador_num2
        resultado = 'P' if total % 2 == 0 else 'I'
        
        print(f'Você escolheu {jogador_num} e o computador escolheu {computador_num2}. O total de {total} deu {"Par" if resultado == "P" else "Ímpar", "I"}')
        
    if jogador_esc == resultado:
        print('Você Venceu!')
        contador += 1
    else:
        print('Você Perdeu!')
        break
    
print(f'Fim de Jogo! Você venceu {contador} vezes consecutivas')
