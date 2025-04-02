#(Variáveis compostas) Listas []

'''num = (2, 5, 9, 1) #criando um tupla
print(num)'''

#Modificando exibira um erro
'''num =(2, 5, 9, 1)
num[2] = 3           # Exemplo que tuplas são Imutáveis
print(num)'''

#Criando uma lista []
'''num = [2, 5, 9, 1]
print(num)'''

'''num = [2, 5, 9, 1]  #Exemplo de uma lista são mutáveis
num [2] = 3        # Saída: o 9 na lista vai ser substituido por 3
print(num)'''


'''num = [2, 5, 9, 1]
num [2] = 3
num[4] = 7        # Saída vai dar erro, porque não pode adicionar valores desta maneira
print(num)'''
 
 
'''num = [2, 5, 9, 1]
num [2] = 3
num.append(7) #Adicionando um alemento
print(num)'''

'''num = [2, 5, 9, 1]
num [2] = 3
num.append(7) 
num.sort() #Colocando em ordem
print(num)'''

'''num = [2, 5, 9, 1]
num [2] = 3
num.append(7) 
num.sort(reverse= True) #Colocando em reverso
print(num)'''

'''num = [2, 5, 9, 1]
num [2] = 3
num.append(7)
num.sort(reverse= True)
print(num)
print(f'Esta lista tem {len(num)} elementos.') #Utilizando len para contar quantos elementos tem'''

#Adiconando valores
'''num = [2, 5, 9, 1]
num [2] = 3
num.append(7)
num.sort(reverse= True)
num.insert(2,0) #Inserindo o elemntos
print(num)
print(f'Esta lista tem {len(num)} elementos.')'''

#Removendo elementos
'''num = [2, 5, 9, 1]
num [2] = 3
num.append(7)
num.sort(reverse= True)
num.insert(2,0) 
num.pop()
print(num)
print(f'Esta lista tem {len(num)} elementos.')'''

'''Eliminando um número'''
'''num = [2, 5, 9, 1]
num [2] = 3
num.append(7)
num.sort(reverse= True)
num.insert(2,0) 
num.pop(2)
print(num)
print(f'Esta lista tem {len(num)} elementos.')'''

'''Um elemento qwue já exista'''
'''num = [2, 5, 9, 1]
num [2] = 3
num.append(7)
num.sort(reverse= True)
num.insert(2,2)  #colocando elementos em posições
print(num)
print(f'Esta lista tem {len(num)} elementos.')'''

#Removendo
'''num = [2, 5, 9, 1]
num [2] = 3
num.append(7)
num.sort(reverse= True)
num.insert(2, 2)
num.remove(2)
print(num)
print(f'Esta lista tem {len(num)} elementos.')'''

'''num = [2, 5, 9, 1]
num [2] = 3
num.append(7)
num.sort(reverse= True)
num.insert(2,2) 
num.remove(4) # Saída dara erro pois ele não esta na lista...
print(num)
print(f'Esta lista tem {len(num)} elementos.')'''

'''Exemplo utilizando for'''

'''num = [2, 5, 9, 1]
num [2] = 3
num.append(7)
num.sort(reverse= True)
num.insert(2,2) 
if 4 in num:
    num.remove(4) 
else:
    print('Tente Novamente! Não foi identificado o número 4')
    
print(num)
print(f'Esta lista tem {len(num)} elementos.')'''

'''num = [2, 5, 9, 1]
num [2] = 3
num.append(7)
num.sort(reverse= True)
num.insert(2,2) 
if 5 in num:
    num.remove(5) # Removendo 5 que esta na lista!
else:
    print('Tente Novamente! Não foi identificado o número 4')
    
print(num)
print(f'Esta lista tem {len(num)} elementos.')'''

# Mostrando a lista mais organizada

'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)

print(valores)'''

#utilizando for

'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...' , end='')'''
    
'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores): # Com a numeração enumerate
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')'''

'''valores = list()
for cont in range(0, 5):
    
    valores.append(int(input('Digite um valor:')))
for c, v in enumerate(valores): # Com a numeração enumerate
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')'''

#Outros exemplos
'''a = [6, 4, 8, 7]
b = a
b [2] = 8
print(f'A lista A: {a}')
print(f'A lista B: {b}')'''

#Fazendo uma copia 
a = [2, 3, 4, 7]
b = a[:]
b [2] = 8
print(f'A lista A: {a}')
print(f'A lista B: {b}')