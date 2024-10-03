#Gerenciador de pagamentos

print('{:=^40}' .format(' Organização Fyantor '))
preco = float(input('Informe o preço das compras R$:'))

print(''' FORMAS DE PAGAMENTO
      [1] Á VISTA, DINHEIRO OU PIX...
      [2] Á VISTA CARTÃO...
      [3] 2X NO CARTÃO...
      [4] 3X OU MAIS NO CARTÃO...''')
opcao = int(input('Qual é a sua opção?'))


if opcao == 1:
    total = preco - (preco * 10 / 100)

elif opcao == 2:
    total = preco - (preco * 5 / 100)

elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra vai ser parcelada em 2x de {:.2f} SEM JUROS!' .format(parcela))

elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totpar = int(input('Quantas parcelas?'))
    parcela = total / totpar
    print('Sua compra vai ser parcelada em {}x ou mais de R${:.2f} COM JUROS!' .format(totpar, parcela))
    
else:
    total = preco
    print('Opção inválida de pagamento. Considerando preço normal.')

print('Sua compra de R${:.2f} vai custar R${:.2f}:' .format(preco, total))

    
