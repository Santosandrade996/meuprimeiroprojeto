#Dicionários {}
'''pessoas = {'nome': 'Giselle', 'idade': 25, 'sexo': 'F'}
print(pessoas['nome'])
print(pessoas['idade'])
print(pessoas['sexo']) '''

# ou pode fazer um print formatado
'''pessoas = {'nome': 'Giselle', 'idade': 25, 'sexo': 'F'}
print(f'O ª {pessoas["nome"]} tem {pessoas["idade"]} anos e o sexo é {pessoas["sexo"]}:.')'''

#Com a utilização do keys() o que retorna todas as chaves
'''pessoas = {'nome': 'Giselle', 'idade': 25, 'sexo': 'F'}
print(pessoas.keys())  # Saida : dict_keys(['nome', 'idade', 'sexo'])'''

#Com o valor values() retorna os valores
'''pessoas = {'nome': 'Giselle', 'idade': 25, 'sexo': 'F'}
print(pessoas.values ()) # Saida : dict_values(['Giselle', 25, 'F'])'''

# Coma a utilização items() pares de chaves valor
''''pessoas = {'nome': 'Giselle', 'idade': 25, 'sexo': 'F'}
print(pessoas.items()) #Saida : dict_items([('nome', 'Giselle'), ('idade', 25), ('sexo', 'F')])'''

#Chaves, valores e os items utilizando laços Keys()
'''pessoas = {'nome': 'Giselle', 'idade': 25, 'sexo': 'F'}
for k in pessoas.keys():
    print(k)'''

#Com values()
'''pessoas = {'nome': 'Giselle', 'idade': 25, 'sexo': 'F'}
for k in pessoas.values():
    print(k)'''

#Com items()
'''pessoas = {'nome': 'Giselle', 'idade': 25, 'sexo': 'F'}
for k, v in pessoas.items():
    print(f'{k} = {v}')'''
    
#Apagando o elemento
'''pessoas = {'nome': 'Giselle', 'idade': 25, 'sexo': 'F'}
del pessoas ['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')'''
 
#Substituindo nomes   
'''pessoas = {'nome': 'Giselle', 'idade': 25, 'sexo': 'F'}
pessoas['nome'] = 'Maria'
for k, v in pessoas.items():
    print(f'{k} = {v}')'''

#Adicionar 
'''pessoas = {'nome': 'Giselle', 'idade': 25, 'sexo': 'F'}
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')'''
    
# Criando dicionario dentro de uma lista
'''brasil = []
estado1 = {'uf': 'Paraná', 'sigla' : 'PR'}
estado2 = {'uf': 'Riode Janeiro', 'sigla' : 'RJ'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)'''

#Com dicionarios dentro de outros 
'''print(brasil)'''
# Estado adiconado primeiro
'''print(brasil[0])'''
# Estado adiconado Segundo
'''print(brasil[1])'''
#Pegando elementos
'''print(brasil[0] ['uf'])'''
#Pegando outros elementos
'''print(brasil[1] ['sigla'])'''

#  Erro de fazer copia
'''estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] =str(input('Sigla do Estado: '))
    brasil.append(estado[:])
print(brasil)'''

#Um metodo utilizando .copy()
'''estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] =str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)'''

#para deixar mais bonito 
'''estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] =str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    print(e)'''

#Para deixar mais bonito ainda
'''estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] =str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
  for k, v in e.items():
      print(f'O campo {k} tem o valor {v}...')'''
      
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] =str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for v in e.values():
        print(v, end=' ')  
    print()
      