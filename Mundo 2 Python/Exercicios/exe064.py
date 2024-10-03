#Desconsiderando flag
'''Esse exemplo é mais detalhado
numero = 0
contador = 0
soma = 0'''

#Simplificado
numero = contador = soma = 0
numero = int(input('Digite um número [999 para parar!]:')) #Lendo o flag do lado de fora 

while numero != 999:
    soma += numero
    contador = contador + 1
    numero = int(input('Digite um número [999 para parar!]:')) #lendo flag do lado de dentro
print('Você digitou {} números e a soma entre eles foram {}' .format(contador, soma))

    