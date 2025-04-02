import random
from time import sleep

resultados = {}

for i in range(1,5):
    resultados[f'Jogador {i}'] = random.randint(1,6)
print('-=' * 30)
print('             Resultados dos jogadores:               ')
print('-=' * 30)
for jogador, resultado in resultados.items():
    print(f'{jogador}: {resultado}')
    sleep(2)

maior_resultado = max(resultados.values())

# Encontrando os jogadores que empataram
vencedores = [jogador for jogador, resultado in resultados.items() if resultado == maior_resultado]

# Exibindo os vencedores
if len(vencedores) > 1:
    print(f"\nHouve um empate entre: {', '.join(vencedores)} com o número {maior_resultado}.")
else:
    print(f"\nO vencedor é {vencedores[0]} com o número {maior_resultado}.")

