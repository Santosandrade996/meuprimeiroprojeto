# Contando maior ou menor de idade

menores_idade = 0
maiores_idade = 0

for i in range(1,8):
    ano_nascimento = int(input(f'Seu ano de nascimento {i}º:'))
    
    idade = 2024 - ano_nascimento
    
    if idade < 18:
        menores_idade += 1
    else:
        maiores_idade += 1
        
print(f'Pessoas menores de idade: {menores_idade}')
print(f'Pessoas Maiores de idade: {maiores_idade}')

 