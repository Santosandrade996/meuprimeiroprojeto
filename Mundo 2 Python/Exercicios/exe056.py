#Analisador completo
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
homem_velho = ''
tot_mulher20 = 0

for p in range(1,5):
    print(f'-------- {p}ª PESSOA --------')
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip().upper()
    soma_idade += idade
    
    if p == 1 and sexo in 'M':
        maior_idade_homem = idade
        homem_velho = nome
    if sexo in 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        homem_velho = nome
    if sexo in 'F' and idade < 20:
        tot_mulher20 += 1

media_idade = soma_idade / 4
print(f'A média de idade do grupo é de {media_idade} anos...')
print(f'O homem mais velhor tem {maior_idade_homem} anos e se chama {homem_velho}')
print(f'Ao todo são {tot_mulher20} mulheres com menos de 20 anos!')
