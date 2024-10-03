#Fibonacci
n = int(input('Digite a quantidade de termos da sequência de fibonacci:'))

termo1, termo2 = 0,1
contador = 0
print('Sequência de fibonacci:')
while contador <= n:
    print(termo1, end=' ')
    
    proximo_termo = termo1 + termo2
    termo1 = termo2
    termo2 = proximo_termo
    contador += 1
    
print()
