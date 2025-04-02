# Coreções/ Boletim com listas compostas
ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1= float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    respo = str(input('Quer conttinuar? [S/N]')).strip().upper()
    
    if respo in 'N':
        break
print('-=' * 30)
print(ficha)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('-' * 26)

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
    
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (Digite 999 para encerrar o programa): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha)- 1:
        print(f'Notas de {ficha[opc] [0]} são {ficha[opc] [1]}')
print('<<< Volte Sempre! >>>')
    