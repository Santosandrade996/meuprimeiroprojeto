#Numeros inteiros
def comparar_numeros(num1, num2):
    if num1 > num2:
        return 'O primeiro valor é maior'
    elif num2 > num1:
        return 'O segundo valor e maior'
    else:
        print('Não existe um valor maior! Os dois São iguais...')

    def main():
        num1 = int(input('Digite o primeiro valor:'))
        num2 = int(input('Digite o segundo valor:'))

        resultado = comparar_numeros(num1, num2)
        print(resultado)

    main()
