#Palindromo
'''frase = str(input('Digite uma frase:')).strip().upper()  #Com a utilização do for
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len (junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}' .format(junto, inverso))
if inverso == junto:
    print('È um palíndromo!')
else:
    print('Ele não é um palíndromo!')'''

frase = str(input('Digite uma frase:')).strip().upper() #Utilizando na forma simplificada com fatiamento...
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}' .format(junto, inverso))

if inverso == junto:
    print('Èle é um palíndromo!')
else:
    print('Èle não é um palíndromo!')
    