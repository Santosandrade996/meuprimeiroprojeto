print('-=' * 30)
print('Matriz 3x3- Parte 1')
print('-=' * 30)

matriz = [[0 for _ in range(3)] for _ in range (3)]

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite o valor para a posição ({i} , {j}):'))
    
print('-=' * 30)
print(f'\nMatriz 3x3:')
for linha in matriz:
    print(' '.join(f'{valor:^5}' for valor in linha))
    
    