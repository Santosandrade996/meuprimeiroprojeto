#seis numeros inteiros
 
soma = 0

for i in range(7):
    numero = int(input(f'Digite o {i + 1}º número:'))
    if numero % 2 ==0:
        soma += numero
print(f'A soma dos números pares digitados é: {soma}')

 