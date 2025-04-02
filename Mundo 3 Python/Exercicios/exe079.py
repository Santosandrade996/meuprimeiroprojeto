numeros = list ()
while True:
    n = int(input('Digite um valor:'))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado...')
    else:
        print('Este valor já foi adicionado,Tente outro valor!')
    r = str(input('Quer continuar? [s/n]'))
    if r in 'Nn':
        break
print('-=' *30)
numeros.sort()
print(f'Você digitou os valores {numeros}')

