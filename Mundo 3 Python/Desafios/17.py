import random
print('-=' * 30)
print('Jogo da mega sena')
print('-=' * 30)

quantidade_jogos = int(input('Qantos jogos deseja gerar?'))

jogos = []

for _ in range(quantidade_jogos):
    palpite = random.sample(range(1, 61), 6)
    
    palpite.sort()
    jogos.append(palpite)

print('-=' * 30)
print('\nPalpites gerados para a Mega Sena:')
print('-=' * 30)

for i, jogo in enumerate(jogos, start=1):
    print(f'Jogo {i}: {jogo}')
    
