#Progressão aritmética v3.0
'''Vou deixar tres progressões aritméticas desde do for ate com a utilização while'''
#1-Com a utilização do for
'''print('-=-' * 10)
print('Progressão Aritmética v1.0')
print('-=-' * 10)

primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    print(f'{c} > ' , end=' ')
print('Fim')'''

#2- Com a utilização do While
'''print('-=' * 20)
print('Progressão Aritmética v2.0')

primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
termo = primeiro
contador = 1

while contador <= 10:
    print(f'{termo} -', end=' ')
    termo += razao
    contador += 1
print('Fim')'''

#3- Com a utilização do while com mais recursos...
print('-=' * 20)
print('Gerador de Progressão Aritmética v3.0')
print('-=' * 20)

primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão:'))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{termo} ->', end=' ') 
        termo += razão
        contador += 1
    print('Pausa')
    mais = int(input('Deseja por outros termos para mostrar mais:'))
print(f'Progressão foi finalizada com {total} de termos mostrado na tela:')
print('Fim')

