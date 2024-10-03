#Com a utilização break

soma = 0
contador = 0

while True:
    numero = int(input('Digite um número  que seja inteiro. [Para finalizar digite 999!]:'))
    
    if numero == 999:
        
        break
    soma += numero
    contador += 1
    
print(f'Os números digitados foram {contador} e a soma entre eles {soma}.')
