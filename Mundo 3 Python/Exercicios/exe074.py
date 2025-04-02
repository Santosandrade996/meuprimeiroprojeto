# Tuplas Sorteio

'''from random import randint
num = (randint(1,10)) Simples
numeros = (randint(1,10), randint(1,10), 
     randint(1,10), randint(1,10), 
     randint(1,10)) # Composta
print(f'Eu sorteei os valores {numeros}')'''

from random import randint
numeros = (randint (1,10), randint(1,10), 
     randint(1,10), randint(1,10), 
     randint(1,10))
print('Os valores sorteados foram:' , end= '')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min (numeros)}')

