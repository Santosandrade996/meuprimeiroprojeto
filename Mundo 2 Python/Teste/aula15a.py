#Interrompendo repetições while (break)
'''contador = 1
while True:
    print(contador, ' > ' , end='')
    contador += 1
print('Fim')'''

'''numero = contador = 0
while contador < 5:
    numero = int(input('Digite um número:'))
    contador = contador + 1'''


'''numero = 0
while numero != 999:  #Utilizção com flag
  numero = int(input('Digite um número:'))'''
  
'''numero = s = 0
while numero != 999:
    numero = int(input('Digite um número:'))
    s+= numero
s -= 999
print(f'A soma vale {s}')'''

numero = s = 0
while True: #Looping infinito
    numero = int(input('Digite um número'))
    if numero == 999:
        break
    s += numero
print(f'A soma vale {s}')



