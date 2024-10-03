#Analise de dados do grupo
print('-=' * 20)
print('Cadastre uma pessoa')
print('-=' * 20)

total = total_de_homens = mulher_menos_20 = 0
while True:
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo: [M/F]')).strip().upper()[0]

    if idade >=18:
        total += 1
    if sexo == 'M':
        total_de_homens += 1
    if sexo == 'F' and idade < 20:
        mulher_menos_20 += 1
    resposta = ' '       
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Total de pessoas com mais de de 20 anos é {total}')
print(f'Homens cadastrados são de {total_de_homens}:')
print(f'Mulheres com menos de 20 anos tem no total {mulher_menos_20}:')
