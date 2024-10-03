#eletronico
print('-=' * 50)
print('Bem vindo ao caixa eletronico!')
print('-=' * 50)

valor_saque = int(input('Digite o valor a ser sacado: R$'))

valor_restante = valor_saque

print('Cédulas entregues:')
while True:
    if valor_restante >= 50:
        cedulas_50 = valor_restante // 50
        valor_restante %= 50
        print(f'Cédulas de R$50: {cedulas_50}')
    if valor_restante >= 20:
        cedulas_20 = valor_restante // 20
        valor_restante %= 20
        print(f'Cédulas de R$20: {cedulas_20}')
    if valor_restante >= 10:
        cedulas_10 = valor_restante // 10
        valor_restante %= 10
        print(f'Cédulas de R$10: {cedulas_10}')
    if valor_restante >= 1:
        cedulas_1 = valor_restante // 1
        valor_restante %= 1
        print(f'Cédulas de R$1: {cedulas_1}')
    
    if valor_restante == 0:
        break
