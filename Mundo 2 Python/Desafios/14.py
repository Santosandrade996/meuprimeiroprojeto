#Tabuada v1.2 Com a utilização do for

numero = int(input('Digite um número para ver a tabuada: '))

print('-' *25)
for tabuada in range(1, 50):
    print('{} * {:2} = {:.2f}' .format(numero, tabuada, numero * tabuada))
print('-' *25)
