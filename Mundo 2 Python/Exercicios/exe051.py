#Progressão aritmetica
print('-' * 50)
print('10 Termos de um progressão aritmética')
print('-' * 50)

primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
decimo = primeiro + (10 - 1) * razao

for c in range (primeiro, decimo + razao, razao):
    print('{}' .format(c), end=' > ')
print('Acabou')