#Estrutura de repetição WHILE...
'''for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('Fim')'''

'''n = 1
while n != 0: #Chamamos de ponto de parada, condição de parada.
    n = int(input('Digite um valor:'))
print('Fim...')'''

#Outro exemplo...
'''r = 'S'
while r == 'S':
    n = int(input('Digite o valor:'))
    r = str(input('Quer continuar? [S/N]')).upper()
print('Fim...')'''

#Mais um exemplo...
'''n = 1
while n != 0:
    n = int(input('Digite um valor:'))
print('Acabou...')'''

#Lendo pares e impares
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor:'))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares!')
