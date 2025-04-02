print('-=' * 30)
print('Índice de Massa Corporal')
print('-=' * 30)

pessoas = []

while True:
    nome = input('Nome: ')
    peso = float(input('Peso (KG): '))
    altura = float(input('Altura (m): '))
    
    pessoas.append([nome, peso, altura])
    
 
    continuar = input('Deseja cadastrar outra pessoa? (S/N): ').strip().upper()
    
  
    if continuar == 'N':
        break

print('-=' *30)
print(f'\nNúmero total de pessoas cadastradas: {len(pessoas)}')

maior_peso = []
menor_peso = []
maior_peso_valor = 0
menor_peso_valor = float('inf')


for pessoa in pessoas:
    nome, peso, altura = pessoa
    imc = peso / (altura ** 2)  # Cálculo do IMC
    
    # Determina o maior e menor peso
    if peso > maior_peso_valor:
        maior_peso_valor = peso
        maior_peso = [nome]
    elif peso == maior_peso_valor:
        maior_peso.append(nome)
    
    if peso < menor_peso_valor:
        menor_peso_valor = peso
        menor_peso = [nome]
    elif peso == menor_peso_valor:
        menor_peso.append(nome)

    
    atividade_fisica = input(f'{nome} faz atividades físicas regularmente? (S/N): ').strip().upper()
    if atividade_fisica == 'S' and imc > 25:
        print(f'⚠️ Alerta: {nome} faz atividades físicas, mas está acima do peso normal. IMC: {imc:.2f}')

# Mostrando resultados
print(f"\nPessoas com maior peso ({maior_peso_valor} kg): {', '.join(maior_peso)}")
print(f"Pessoas com menor peso ({menor_peso_valor} kg): {', '.join(menor_peso)}")
