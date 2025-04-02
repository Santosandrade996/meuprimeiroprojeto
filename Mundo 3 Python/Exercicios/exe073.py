#Tuplas com Time de Futebol

times = ('Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'São Paulo', 'Bahia', 'Internacional', 'Cruzeiro', 'Vasco da Gama', 'Atlético-MG', 'Criciúma', 'Bragantino', 'Juventude', 'Grêmio', 'Athletico-PR', 'Fluminense', 'EC Vitória', 'Corinthians', 'Cuiabá', 'Atlético-GO')
print('-=' * 90)
print (f'Lista de times: {times}')
print('-=' * 90)
print('-=' * 90)
print(f'Os 5 primeiros são: {times [0:5]}')
print('-=' * 90)
print(f'Os quatro últimos são: {times[-4:]} ')
print('-=' * 90)
print(f'Times em ordem alfabética: {sorted(times)}') #Sorted coloca na ordem alfabetica
print('-=' * 90)
print(f'O Cruzeiro esta na {times.index("Cruzeiro")+1}ª posição')

