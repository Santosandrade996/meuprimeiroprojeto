#Fatorial
numero = int(input('Digite um número qualquer:'))

if numero < 0:
    print('Fatorial não é definido para números negativos ')
else:
    fatorial = 1
    contador = 1
    
    while contador <= numero:
        fatorial *= contador
        contador += 1
        
        print(f'{numero}! = {fatorial}')
        