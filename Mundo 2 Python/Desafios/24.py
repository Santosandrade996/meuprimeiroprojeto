#Criando opções
print('=' *30)
print('''
      Menu
      [1] Somar
      [2] subtrair
      [3] Multiplicar
      [4] Dividir
      [5] Maior
      [6] Menor
      [7] Novos números
      [8] Sair do programa''')
print('=' * 30)

valor_1 = float(input('Digite o primeiro valor:'))
valor_2= float(input('Digite o segundo valor:'))

while True:
    opcao = int(input('Escolha uma opção:'))
    
    if opcao == 1:
        print(f' A soma de {valor_1} + {valor_2} é igual a {valor_1 + valor_2}')
    elif opcao == 2:
        print(f'A subtração de {valor_1} - {valor_2} é igual a {valor_1 - valor_2}')
    elif opcao == 3:
        print(f'A multiplicação do {valor_1} * { valor_2} é igual a {valor_1 * valor_2}')
    elif opcao == 4:
        print(f'A divisão do {valor_1} / {valor_2} é igual a {valor_1 / valor_2} ')
    elif opcao == 5:
        print(f'O maior número entre {valor_1} e {valor_2} é  {max(valor_1, valor_2)}')
    elif opcao == 6:
        print(f'O menor valor entre {valor_1} e {valor_2} é {min(valor_1, valor_2)}')
    elif opcao == 7:
        valor_1 = float(input('Digite um novo número:'))
        valor_2 = float(input('Digite um novo segundo número:'))
    elif opcao == 8:
        print('Saindo do programa...')
        break
    else:
        print('Opção Invalida! Escolha a opção entre 1 a 6')

print('Programa Encerrado...')