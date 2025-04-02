print('-=' * 30)
print('                 Média do aluno               ')
print('-=' * 30)

aluno = {}

aluno['nome'] = input('Digite o nome do aluno:')
aluno['media'] = float(input(f'Digite a Média do aluno {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'
    
for chave, valor in aluno.items():
    print(f'{chave.capitalize()}: {valor}')
    
