#Estatisticas do produto
total = total_mil = menor = contador = 0
barato = ''
while True:
    produto = str(input('Nome do produto:')).strip().upper()[0]
    preço = float(input('Valor do produto: R$'))
    contador += 1
    total += preço
    
    if preço > 1000:
        total_mil += 1
    if contador == 1 or preço < menor: #simplificado
        menor = preço
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
         break
print('{:-^40}' .format('Fim do programa!'))
print(f'As compas ficaram no total R${total:.2f}')
print(f'Total de {total_mil} produtos custa mais de R$1000.00')
print(f'O menor preço do produto é R${menor:.2f}')
print(f'O nome do prduto barato é {barato}')