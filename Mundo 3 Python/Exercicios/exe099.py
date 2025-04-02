# Função qie descobre o maior
from time import sleep


def maior(*num):
    contador = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.4)
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(f'foram informados  {contador} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
    
    
# Programa principal
maior(57, 68, 40, 35, 90, 378, 26, 38)
maior(7, 9,10, 30, 28, 78, 56, 3)
maior(0)
maior()