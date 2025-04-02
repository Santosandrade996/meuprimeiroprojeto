#Números extensos
numeros_extensos = ('0' , '1', '2', '3', '4', '5', '6', '7', '8', '9', 
           '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20')


numero = int(input('Digite um número de 0 e 20:'))

if 0 <= numero <= 20:
    print(f'o número {numero} por extenso é: {numeros_extensos [numero]}')
else:
    print(f'Número esta Invalido! Digite novamente...')
    
    