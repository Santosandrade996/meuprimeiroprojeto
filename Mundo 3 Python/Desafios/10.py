valores = []

while True:
    num = int(input('Digite um número (ou -1 para sair ):'))
    
    if num == -1:
        break
    
    valores.append(num)
    
    quantidade = len(valores)
    
    valores.sort(reverse = True)
    
    tem_cinco = 5 in valores
    
print(f'\nQuantidade de números digitados: {quantidade}')
print(f'Lista de valores (oredenada na ordem decrescente): {valores}')
print(f'O valor 5 {"está" if tem_cinco else "não está"} na lista.')
