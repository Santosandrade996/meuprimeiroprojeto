#Variáveis compostas-Parte 2
'''teste = list()
teste.append('Giselle')
teste.append(27)
print(teste)'''

'''teste = list()
teste.append('Giselle')
teste.append(27)
galera = list()
galera.append(teste)
print(galera)'''

'''teste = list()
teste.append('Giselle')
teste.append(27)
galera = list()
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 17
galera.append(teste)
print(galera)'''

'''teste = list()
teste.append('Giselle')
teste.append(27)
galera = list()
galera.append(teste[:]) #fazendo uma copia
teste[0] = 'Maria'
teste[1] = 17
galera.append(teste[:]) #Fazendo uma copia
print(galera)'''

'''galera = [ ['Giselle' , 39] , 
          ['Maria alice', 28], 
          ['Jujuba', 67], 
          ['Jorge', 56]
    
]
print(galera)'''


#mostrar os dados do Giselle
'''galera = [ ['Giselle' , 39] , 
          ['Maria alice', 28], 
          ['Jujuba', 67], 
          ['Jorge', 56]
    
]
print(galera[0])'''

#Pegando só o primeiro elemento da lista
'''galera = [ ['Giselle' , 39] , 
          ['Maria alice', 28], 
          ['Jujuba', 67], 
          ['Jorge', 56]
    
]
print(galera[0][0])'''

#Pegando só a idade de jujuba
'''galera = [ ['Giselle' , 39] , 
          ['Maria alice', 28], 
          ['Jujuba', 67], 
          ['Jorge', 56]
    
]
print(galera[2][1])'''

#Com a utilização dp for
'''galera = [ ['Giselle' , 39] , 
          ['Maria alice', 28], 
          ['Jujuba', 67], 
          ['Jorge', 56]
    
]

for p in galera:
    print(p)'''
    
    
'''galera = [ ['Giselle' , 39] , 
          ['Maria alice', 28], 
          ['Jujuba', 67], 
          ['Jorge', 56]
    
]
for p in galera:
    print(p[0])'''
    
    
'''galera = [ ['Giselle' , 39] , 
          ['Maria alice', 28], 
          ['Jujuba', 67], 
          ['Jorge', 56]
    
]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')'''
    
'''galera = list()
dado = list ()
for c in range(0, 5):
    dado.append(str(input('Nome:')))
    dado.append(int(input('Idade:')))
    galera.append(dado{:}) #copia de dados
    dado.clear()
    
print(galera)'''

galera = list() #Criando 2 estruturas
dado = list () #Estrutura de dados é auxiliar que vai pegar os dados principal que é a do galera.
totmai = totmen = 0 #Ver o total e maior e menor de idade

for c in range(0, 5):
    dado.append(str(input('Nome:')))
    dado.append(int(input('Idade:'))) #Fazendo um bloco todo para ler o dados e jogar dentro da galera e apagando os laços cada ves que faz o laço
    galera.append(dado[:]) #copia de dados
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.') #Analiso a cada vez se a pessoa e maior ou menor de idade
        totmai+= 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen+= 1
print(f'Temos {totmai} maiores e {totmen} menores de idade...') #saida