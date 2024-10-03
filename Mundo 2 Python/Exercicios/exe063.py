print('-' * 30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar?'))

termo_1 = 0
termo_2 = 1
print('~' *30)
print(f'{termo_1} > {termo_2}', end='')
contador = 3
while contador <= n:
    termo_3 = termo_1 + termo_2
    print(f' > {termo_3}' , end='')
    termo_1 = termo_2
    termo_2 = termo_3
    contador += 1
print(' > Fim')
print('~' *30)