#Correção de base numericas

numero = int(input('Digite um numero que seja inteiro:'))
print('''Escolha uma das bases para conversão:
      [1] converter para binario
      [2] converter para octal
      [3]converter para hexadecimal''')
opcão = int(input('Sua opção:'))

if opcão == 1:
    print('{} convertido para binario é igual: {}' .format(numero, bin(numero)[2:]))
elif opcão == 2:
    print('{} convertido para octal é igual: {}' .format(numero, oct(numero)[2:]))
elif opcão == 3:
    print('{} convertido em hexadecimal é igual: {}' .format(numero, hex(numero)[2:]))
else:
    print('Opção Invalida! Tente novamente!')
    
