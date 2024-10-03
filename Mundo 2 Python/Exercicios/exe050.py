# Soma dos pares
soma  = 0
contador = 0
for cont in range(1, 7):
    numero = int(input('Digite o {}º valor:' .format(cont)))
    if numero % 2 == 0:
        soma += numero
        contador += 1
print('Você informou {} números PARES e a soma foi {}' .format(contador, soma))
