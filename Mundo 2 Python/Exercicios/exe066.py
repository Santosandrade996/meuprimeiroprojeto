#Vários números com flag
#Com gambiarra
'''num = soma = 0
while num != 999:
    num = int(input('Digite um valor: (999 para parar):'))
    soma += num
soma-= 999
print(f'A soma dos valores foi {soma}')'''

#organizando os codigos sem gambiarra
soma = cont = 0 
while True:
    numero = int(input('digite um valor (999 para parar):'))
    if numero == 999:
        break
    cont += 1
    soma += numero
print(f'A soma dos {cont} valores foi {soma}!')

