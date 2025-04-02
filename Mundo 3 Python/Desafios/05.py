#Em forma tabular
produtos_precos = (
    ('Tenis Adidas', 378.00),
    ('Diavolo' , 145.00),
    ('Mizuno ', 265.00),
    ('Under Armour', 347.90),
    ('Asics', 567.87)    
)


print(f"{'Produto' : <15} {'Preço':<10}")
print('-' * 30)

for produto, preco in produtos_precos:
    print(f"{produto:<15} R$ {preco:.2f}")
    