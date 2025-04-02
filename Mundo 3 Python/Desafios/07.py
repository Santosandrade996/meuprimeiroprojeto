'''numeros = []

for i in range(5):
    valor = input(f'Digite um valor para a posição {i} (ou digite "sair" para parar):')
    
    if valor.lower() == 'sair': # Fazendo a verificação caso o usuário quiser intemrromper a entrada
        print("Interrupção pelo usuário. Entrada de dados finalizada...")
        break
    
    numeros.append(int(valor))
    
if numeros:
    maior_valor = max(numeros)
    menor_valor = min(numeros)
    
    print(f'\nVocê digitou os valores: {numeros}')
    print(f'O maior valor digitado foi {maior_valor} nas posições' , end=' ')
    
    for i, v in enumerate(numeros):
        if v == maior_valor:
            print(f"{i}..." , end=' ')
else:
    print('Nenum valor foi inserido.')'''
    
'''numeros = [ int(input('Digite o Primeiro valor:')),
            int(input('Digite o Segundo valor:')),
            int(input('Digite o Terceiro valor:')),
            int(input('Digite o Quarto valor:')),
            int(input('Digite o Quinto valor:'))
           
]
maior_valor = max(numeros)
menor_valor = min(numeros)

print(f'\nVocê digitou os valores: {numeros}')
print(f'O maior valor digitado foi {maior_valor} nas posições', end=' ')

for i, v in enumerate(numeros):
    if v == maior_valor:
        print(f'{i}...', end=' ')
        
print(f'\nO menor valor digitado foi {menor_valor} nas posições', end=' ')

for i, v in enumerate(numeros):
    if v == menor_valor:
        print(f"{i}...", end=' ')'''
        
numeros = [ int(input('Digite o Primeiro valor:')),
            int(input('Digite o Segundo valor:')),
            int(input('Digite o Terceiro valor:')),
            int(input('Digite o Quarto valor:')),
            int(input('Digite o Quinto valor:'))
]

for i in range(5):
    valor = int(input(f"Digite o {i + 1}º valor: "))
    numeros.append(valor)

    
    continuar = input("Quer continuar? (s/n): ").strip().lower()
    if continuar == 'n':
        print("Interrupção pelo usuário. Entrada de dados finalizada.")
        break


if numeros:
    maior_valor = max(numeros)
    menor_valor = min(numeros)

    
    print(f"\nVocê digitou os valores: {numeros}")
    print(f"O maior valor digitado foi {maior_valor} nas posições ", end='')

    for i, v in enumerate(numeros):
        if v == maior_valor:
            print(f"{i}...", end=' ')

    print(f"\nO menor valor digitado foi {menor_valor} nas posições ", end='')

    for i, v in enumerate(numeros):
        if v == menor_valor:
            print(f"{i}...", end=' ')
else:
    print("Nenhum valor foi inserido.")