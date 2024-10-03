#Calculo Fatorial
#Forma simplificada usando importação
'''from math import factorial

n = int(input('Digite um número para calcular seu fatorial:'))
f = factorial (n)
print(f'O fatorial de {n} é {f}')'''

#Fazendo sem utilizar importações
n = int(input('Digite um número para calcular seu fatorial:'))
c = n
f = 1
print(f'Calculando {n}! =', end=' ')
while c > 0:
    print(f'{c}' , end=' ')
    print('x' if c > 1 else ' = ' , end=' ')
    f *= c
    c -= 1
print(f'{f}')