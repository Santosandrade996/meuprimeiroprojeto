#Peso de sete pessoas 

maior_peso = 0
menor_peso = float('inf') # inicializa com infinito para garantir que qualquer peso lido será menor

for i in range(1,8):
    peso = float(input(f'Digite o peso da {i}º pessoa em kg:'))
    
    # Verifica se o peso atual é o maior ou o menor peso lido até agora
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso
print(f'O maior peso lido foi: {maior_peso} kg')
print(f'O menor peso lido foi: {menor_peso} kg')
