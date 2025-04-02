#Unindo dicionários e lista

galera = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
            pessoa['sexo']= str(input('Sexo: [M/F]')).upper()[0]
            if pessoa['sexo'] in 'MF':
                break
            print('ERRO! Digite novamente apnas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        respo = str(input('Quer continuar? [S/N] ')).upper()[0]
        if respo in 'SN':
            break       
        print('ERRO! Responda apenas S ou N...')     
    if respo == 'N':
        break

print('=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos...')
print('As mulheres cadastradas foram', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print('Lista de pessoas acima da média:')
for p in galera:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('<< Encerrado >>')

