#Simulador de caixa eletronico
print('=' * 40)
print('{:^40}' .format('Banco do aprendizado'))
print('=' * 40)

valor = int(input('Digite o valor para sacar? R$'))
total = valor
cedula = 50
total_cedula = 0
while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
print('=' * 90)
print('obrigado por nos escolher! Volte sempre ao Banco do aprendizado! Tenha um bom dia!')
print('=' * 90)
