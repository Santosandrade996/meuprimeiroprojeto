#Tabuada versão 2
numero = int(input('Digite qualquer número para consultar sua tabuada de Multiplicação:'))

print('-' * 20)
for tabuada in range(1, 50):
    print('{} x {:2} = {}' .format(numero, tabuada, numero * tabuada))

print('-' * 20)
