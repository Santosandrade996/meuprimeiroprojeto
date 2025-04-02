#Listagem de preços em um tupla

listagem = (
    ('Tenis Adidas', 378.00),
    ('Diavolo' , 145.00),
    ('Mizuno ', 265.00),
    ('Under Armour', 347.90),
    ('Asics', 567.87)    
)
print('-=' * 30)
print(f'{"Listagem de Precos" :^40}')
print('-=' * 30)

for item in listagem:
    nome = item[0] # Vai acessar o nomes do produtos
    preco = item[1] # Vai acessar os preços do produtos
    print(f'{nome:.<30} R$ {preco: >7.2f}')
print('-=' * 30)

