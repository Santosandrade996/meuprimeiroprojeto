#Nomes e preços

gasto = 0
produto_maior_1000 = 0
produto_baratonome = ''
produto_mais_barato_preco = None

while True:
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o valor do produto: R$'))
    gasto += preco
    
    if preco > 1000:
        produto_maior_1000 += 1
    if produto_mais_barato_preco is None or preco < produto_mais_barato_preco:
        produto_mais_barato_preco = preco
        produto_baratonome = produto
       
    continuar = input('Deseja continuar? [S/N]').strip().upper()
    while continuar not in ('S', 'N'):
        continuar = input('Opção Invalida! Deseja continuar? [S/N]').strip().upper()
        
    if continuar == 'N':
        break
        

print(f'O Total gasto foi {gasto:.2f} em compras')
print(f'O total de produtos {produto_maior_1000} que custaram mais de R$1000')
print(f'O produto mais barato foi {produto_baratonome}')

