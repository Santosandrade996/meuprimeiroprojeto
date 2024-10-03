contador = 0
soma = 0

while True:
    numero = int(input('Digite um número inteiro: (\033[91m999 Finaliza a contagem...)'))
    
    if numero == 999:
        break
    contador += 1
    soma += numero
    
print(f'Você digitou {contador} números.')
print(f'A soma dos números digitados é {soma}')
