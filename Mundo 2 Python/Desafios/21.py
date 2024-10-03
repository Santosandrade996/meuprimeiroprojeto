# Nome, idade e o sexo de 4 pessoas

total_idade = 0
nome_homem_velho = ''
idade_homem_velho = 0
mulheres_menos_20 = 0

for i in range(1,5):
    print(f'----- {i}º Pessoa -----')
    nome = input('Nome:')
    idade = int(input('Idade:'))
    sexo = input('Sexo (M/F):').strip().upper() # strip(): remove espaços em branco no início e no fim da string
    # upper(): converte todos os caracteres da string para maiúsculas
    total_idade += idade
    
    if sexo == 'M' and idade > idade_homem_velho:
        idade_homem_velho = idade
        nome_homem_velho = nome
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
        
media_idade = total_idade / 4
print(f'A média de idade do grupo é: {media_idade:.1f} anos')
if nome_homem_velho:
    print(f'O homem mais velho é {nome_homem_velho} com {idade_homem_velho} anos')
else:
    print(f'Não há homens no grupo.')

print(f'Há {mulheres_menos_20} mulheres com menos de 20 anos')

     
    