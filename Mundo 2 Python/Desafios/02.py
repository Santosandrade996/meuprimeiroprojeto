#Binario, Octal e Hexadecimal
def decimal_para_binario(numero):
    return bin(numero)[2:]

def decimal_para_octal(numero):
    return oct(numero)[2:]
def decimal_para_hexadecimal(numero):
    hex_result = hex(numero)[2:]
    if len(hex_result) % 2 !=0:
        hex_result = '0' + hex_result
        return hex_result
def conversor_base():
    numero = int(input('Digite um número que seja inteiro...'))

    print('Escolha a base de conversão:')
    print('1. Binário')
    print('2. Octal:')
    print('3. Hexadecimal:')

    opcao = int(input('Digite um número de opção desejado...'))

    if opcao == 1:
        print('O número {} em Binário é: {}'.format(numero, decimal_para_binario(numero)[2:]))
    elif opcao == 2:
        print('O número {} em Octal é: {}'.format(numero, decimal_para_octal(numero)[2:]))
    elif opcao == 3:
        print('O número {} em Hexadecimal é: {}'.format(numero, decimal_para_hexadecimal(numero)[2:]))
    else:
        print('Opção INVALIDA! Por Gentileza escolha uma opção que seja válida')


conversor_base()
