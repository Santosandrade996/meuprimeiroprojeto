boletim = []
numero_alunos = int(input('Qantos alunos você deseja cadastrar?'))

for _ in range(numero_alunos):
    print('-=' * 30)
    nome = input('Insira o nome do aluno:')
    notas = []
    
    for i in range(1, 5):
        nota = float(input(f'Nota do {i}º bimestre:'))
        notas.append(nota)
        
    media = sum(notas) / len(notas)
    boletim.append({'nome': nome, 'notas': notas, 'media': media})
    
#Exibição do boletim 
print('\nBoletim:')
for aluno in boletim:
    print(f'Aluno: {aluno["nome"]} - Média: {aluno["media"]:.2f}')
    
while True:
    print('-=' * 30)
    aluno_procurado = input(f'Digite o nome do aluno para ver as notas (ou "sair" para encerrar... ):')
    if aluno_procurado.lower() == 'sair':
        break
    
    for aluno in boletim:
        if aluno ['nome'].lower() == aluno_procurado.lower():
            print(f'Notas de {aluno["nome"]}: {aluno["notas"]}')
            break
    else:
        print('-=' * 30)
        print("Aluno não encontrado. Tente novamente!")
        
        