#Melhorando a progressão 
print('-' * 60)
print('Progressão aritmética')
print('-' * 60)

primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão:'))

termo_atual = primeiro
contador = 0
 
while contador <= 10:
    print(termo_atual, end=' ')
    termo_atual += razao 
    contador += 1
   
    if contador > 10:
        mais = int(input('\nQuer mostrar mais quantos termos?'))
        contador += mais

print(f'progressão finalizada com {contador} termos mostrados')