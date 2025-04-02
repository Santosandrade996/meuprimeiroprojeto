#Números aleatorios 

import random
numeros = tuple(random.randint(1,100) for _ in range(5))

print(f'Números que foram gerados: {numeros}')
print(f'O maior número do valor gerado foi: {max (numeros)}')
print(f"O menor número do valor gerado foi: {min(numeros)}")
