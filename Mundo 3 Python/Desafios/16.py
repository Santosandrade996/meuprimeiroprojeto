print('-=' * 30)
print('Matriz 3x3 - Parte 2')
print('-=' * 30)

matriz = [[0 for _ in range(3)] for _ in range(3)]
soma_pares = 0
soma_terceira_coluna = 0
maior_segunda_linha = float('-inf')

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite o valor para a posição ({i}, {j}):'))
        
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]
        
        if j == 2:
            soma_terceira_coluna += matriz[i][j]
        if i == 1 and matriz[i][j] > maior_segunda_linha:
                maior_segunda_linha = matriz[i][j]
 
print('-=' * 30)
print(f'\nMatriz 3x3')
for linha in matriz:
    print(' '.join(f"{valor:^5}" for valor in linha))

print('-=' * 30)
print(f'\nSoma dos valores pares: {soma_pares}')
print(f'\nSoma dos valores da terceira coluna: {soma_terceira_coluna}')
print(f'\nMaior valor da segunda linha: {maior_segunda_linha}')
