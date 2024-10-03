#Estrutura de repetição for

#for n in range(0, 6):
   # print('Estrututa de repetição for') #exemplo simples...
#print('FIM...')

#Vou por com uma tabulação a mais...
'''for n in range(0, 7):
    print('ESTRUTURA DE REPETIÇÃO FOR')
    print('FIM...')'''
    
#Jogando fim para fora da tabulação
#for n in range(0, 9):
 #   print('Estou aprendendo não me atrapalhe!')
#print('FIM...')

#Escrevendo pondo a variavel n em print dentro de identação:
'''for n in range(1, 10):
    print(n)
print('FIM...')'''

#Contagem de tal valor e outro valor diferente:
#for n in range(10, 0, -1): #valores de ordem descrescente se põe -1
 #   print(n)
#print('FIM...')'''

#Pulando casas de doi em dois 
'''for n in range(0, 20, 2): #pulando de dois em dois
    print(n)
print('FIM...')'''

#outro exemplo
#n = int(input('Digite um número qualquer:'))
#for c in range(0, n+1):
 #   print(c)
#print('FIM')

#Utilizando outro exemplo
'''i = int(input('Inicio:'))
f = int(input('Fim:'))
p = int(input('Passo:'))
for c in range(i, f+1, p):
    print(c)
print('FIM...')'''

#Fazendo lendo tres vezes ou mais
#for c in range(0, 5):
 #   n = int(input('Digite qualquer valor:'))
#print('Fim')

#Com somatorio
s = 0
for c in range(0,4):
    n = int(input('Digite um valor:'))
    s += n
print('O somatório de todos os valores foi {}' .format(s))
