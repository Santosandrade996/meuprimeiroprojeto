#Progressão aritmetica v2.0
print('Gerador de Prograssão Aritmética v2.0')
print('-=' * 20)
primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão:'))
termo = primeiro
contador = 1

while contador <= 10:
    print(f'{termo} ->', end=' ')
    termo += razão
    contador += 1
print('FIM')

