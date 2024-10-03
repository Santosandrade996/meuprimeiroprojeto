#Pessoas cadastradas
Mais_18 = 0
homens_cadastrados = 0
mulheres_20 = 0

while True:
    idade = int(input('Digite sua idade:'))
    sexo = str(input('Digite o seu sexo: [M/F]')).strip().upper()
    
    while sexo not in ('M', 'F'):
        sexo = input('Sexo Invalido! Digite novamente o seu sexo: [M/F]').strip().upper()
        
        
    if idade < 18:
        Mais_18 += 1
        
    if sexo == 'M':
        homens_cadastrados += 1
        
    if sexo == 'F' and idade < 20:
        mulheres_20 += 1
        
    continuar = input('Quer Continuar? [S/N]').strip().upper()
    while continuar not in ('S', 'N'):
        continuar = input('Opção Invalida! Quer Continuar? [S/N]').strip().upper()
        
    if continuar == 'N':
        break
    
print(f'O total de pessoas {Mais_18} que tem mais de 18 anos')
print(f'O total de homens {homens_cadastrados} cadastrados')
print(f'O total {mulheres_20} mulheres de tem menos de 20 anos')
