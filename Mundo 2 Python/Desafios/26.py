#PA
print('-' * 60)
print('10 Termos de um progressão aritmética utilizando while')
print('-' * 60)

primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
decimo = primeiro + (10 - 1) * razao

termo_atual = primeiro
contador = 1

while contador <=10:
    print(termo_atual, end=' ')
    termo_atual += razao
    contador += 1
print('Acabou')
