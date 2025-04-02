print('-=' *10)
pares = []
impares = []

contador = 0

for i in range(7):
    valor = int(input(f'Digite {i + 1}º valor:'))
    contador += 1
    
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
        
pares.sort()
impares.sort()

print('-=' *30)
print(f'Você digitou {contador} números.')
print(f'Valores pares em ordem crescente: {pares}')
print(f'valores ímpares em ordem crescente: {impares}')

