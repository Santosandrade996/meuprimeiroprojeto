# Correções dos desafios (Números por extenso)

cont = ('0' , '1', '2', '3', '4', '5', '6', '7', '8', '9', 
           '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente Novamente!', end=' ')
print(f'Você digitou o número {cont[num]}') 