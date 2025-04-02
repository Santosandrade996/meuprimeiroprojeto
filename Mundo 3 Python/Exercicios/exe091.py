#jogos de dados
from random import randint
from time import sleep
from operator import itemgetter


jogo= {'jogador 1': randint(1,6), 
       'jogador 2': randint(1,6), 
       'jogador 3': randint(1,6), 
       'jogador 4': randint(1,6) }
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f' -{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(),  key=itemgetter(1), reverse=True)
print('=' * 40)
print('<<<  Ranking dos jogadores    >>>')
for i, v in enumerate(ranking):
    print(f' {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
    