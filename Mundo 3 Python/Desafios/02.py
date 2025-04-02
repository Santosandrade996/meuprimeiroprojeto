#Tabela do campeonato brasileiro serie A
print('=' * 50)
print(' Tabela da serie A Brasileirão 2024')
print('=' * 50)


times_brasileiros = ('Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'São Paulo', 'Bahia', 'Internacional', 'Cruzeiro', 'Vasco da Gama', 'Atlético-MG', 'Criciúma', 'Bragantino', 'Juventude', 'Grêmio', 'Athletico-PR', 'Fluminense', 'EC Vitória', 'Corinthians', 'Cuiabá', 'Atlético-GO')

primeiros_colocados_libertadores = times_brasileiros[:4] #Os quatros colocados da copa da libertadores.
qualificacoes_libertadores = times_brasileiros[4:6] #Os que vão se Qualificar para copa da libertadores.
times_alfabeticos = sorted(times_brasileiros)
zona_rebaixamento = times_brasileiros[16:] #Os que estão na zona de rebaixamento.

print('=' * 60)
print("Os 4 primeiros colocados na copa da libertadores são:")
for time in primeiros_colocados_libertadores:
    print(time)

print('=' * 60)
print("\nTimes nas qualificatórias da libertadores:")
for time in qualificacoes_libertadores:
    print(time)
 
print('=' * 60)   
print("\nLista de times em ordem alfabética:")
for time in times_alfabeticos:
    print(time)

print('=' * 60)
print("\nTimes que estão na zona de rebaixamento da série A:")
for time in zona_rebaixamento:
    print(time)

