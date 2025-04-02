'''Tuplas () ,  [] listas , {} dicionarios'''

#1- antigamente 
'''lanche = 'Hambúrguer'
lanche = 'Suco'
print(lanche)'''
# 2 - Agora
'''lanche = ('Hambúrguer',  'Suco' , 'Pizza', 'Pudim') # Criando uma estrutura composta #Com parenteses
print(lanche)'''

'''lanche = 'Hambúrgue' , 'Suco' , 'Pizza' , 'Pudim' # Sem parenteses
print(lanche)'''

# 3- Usando com listas [] ..
'''lanche = ('Hambúrguer', 'Suco', 'Pizza' , 'Pudim')
print(lanche [0])
lanche = ('Hambúrguer' , 'Suco' , 'Pizza' , 'Pudim')
print(lanche [1])
lanche = ('Hambúrguer' , 'Suco' , 'Pizza' , 'Pudim')
print(lanche [2])
lanche = ('Hambúrguer' , 'Suco', 'Pizza', 'Pudim')
print(lanche [3])'''

# Usando listas [Utilizando -1 adiante]
'''lanche = ('Hambúrguer', 'Suco' , 'Pizza' , 'Pudim')
print(lanche [-1])
lanche = ('Hambúrguer', 'Suco' , 'Pizza' , 'Pudim')
print(lanche [-2])
lanche = ('Hambúrguer', 'Suco' , 'Pizza' , 'Pudim')
print(lanche [-3])
lanche = ('Hambúrguer', 'Suco' , 'Pizza' , 'Pudim')
print(lanche [-0])'''

#Usando listas [Utilizando 1:3 e por diante]
'''lanche = ('Hambúrguer', 'Suco' , 'Pizza' , 'Pudim')
print(lanche [0:1])
lanche = ('Hambúrguer', 'Suco' , 'Pizza' , 'Pudim')
print(lanche [-0:])
lanche = ('Hambúrguer', 'Suco' , 'Pizza' , 'Pudim')
print(lanche [1:3])
lanche = ('Hambúrguer', 'Suco' , 'Pizza' , 'Pudim')
print(lanche [1:2])
lanche = ('Hambúrguer', 'Suco' , 'Pizza' , 'Pudim')
print(lanche [2:])
lanche = ('Hambúrguer', 'Suco' , 'Pizza' , 'Pudim')
print(lanche [:2])'''

'''Tuplas são imutáveis'''
# Exemplo
'''lanche = ('Hambúrguer', 'Suco' , 'Pizza' , 'Pudim')
lanche [1] = 'Refrigerante'''

# Com len
'''lanche = ('Hambúrguer', 'Suco' , 'Pizza' , 'Pudim','Batata frita')
print(len(lanche))'''

# Com for
'''lanche = ('Hambúrguer', 'Suco' , 'Pizza' , 'Pudim')
for comida in lanche:
    print(f'Irei comer {comida}')
print('Comi de encher o bucho!')'''

# Com for e len utilizando duas maneiras:

#lanche = ('Hambúrguer', 'Suco' , 'Pizza' , 'Pudim' 'Batata frita')
#for cont in range(0, len(lanche)): 
 #   print(cont)
 
'''lanche = ('Hambúrguer', 'Suco' , 'Pizza' , 'Pudim', 'Batata frita')
for cont in range (0, len(lanche)):
     print(f'Irei comer {lanche[cont]}')
print('Comi de encher o bucho!')'''

#outra maneira de se fazer

'''lanche = ('Hambúrguer', 'Suco' , 'Pizza' , 'Pudim' 'Batata frita')
for cont in range(0, len(lanche)): 
   print(f' Irei comer {lanche [cont]} na posição {cont}')'''
   
'''lanche = ('Hambúrguer', 'Suco' , 'Pizza' , 'Pudim', 'Batata frita')
for pos, comida in enumerate (lanche):
    print(f'Irei comer {comida} na posição {pos}')
print('Comi de encher o bucho!')'''

# Mais uma maneira
'''lanche = ('Hambúrguer', 'Suco' , 'Pizza' , 'Pudim', 'Batata frita')
print(sorted(lanche)) #Sorted quer dizer organizado
print(lanche)'''

# Criando Tuplas
'''a = (2, 5, 4)
b = (5, 8, 1, 2)
#c = a + b
c = b + a 
print(c)'''
#print(c, b)
# Outro exemplo co len e metodos internos

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a 
print(len(c))'''

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
#c = a + b
c = b + a 
print(c. count(9))'''

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a 
print(c)
print(c. index(2))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a 
print(c)
print(c. index(5, 1)) # se chama deslocamento'''

# Outros exemplos 
'''pessoa = ('Giselle', 28, 'F', 65.77)
print(pessoa)'''

pessoa = ('Giselle', 28, 'F', 65.77)
del(pessoa) # deletando a pessoa da tupla
print(pessoa)                          