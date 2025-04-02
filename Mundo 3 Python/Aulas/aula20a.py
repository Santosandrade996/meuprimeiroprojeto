#Funções
'''def linha():
    print('=' * 55)
    
# Programa principal
linha()
print('              -Aprendendo Funções              ')
print('              -Python é o futuro!              ')
print('              -Parte teorica da aula de funções(def)             ')
linha()'''


'''def linha():
    print('=' * 55)
    
# Programa principal
linha()
print('              -Aprendendo Funções              ')
linha()
print('              -Python é o futuro!              ')
linha()
print('              -Parte teorica da aula de funções(def)             ')
linha()'''

'''def titulo(txt):
    print('-=' * 35)
    print(txt)
    print('-=' * 35)

#Programa principal`
titulo('                Curso de python             ')
titulo('                Aprendendo Funções (def)    ')
titulo('                Python é o futuro!       ')'''

'''def soma(a, b):
    s = a + b
    print(s)


#Programa Principal
soma(4, 5)
soma(8,9)
soma(2,1)
soma(4, 1)'''



''''def soma(a, b):
    s = a + b
    print(s)


#Programa Principal
soma(a=4, b=5)
soma(b=4, a=5)'''

'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    print(s)


#Programa Principal
soma(a=4, b=5)

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    print(s)


#Programa Principal
soma(b=4, a=5)
soma(7,2)
soma(3, 9, 5)'''

'''def contador(*num):
    print(num)
    

contador(2, 1, 7)
contador(3, 7, 8, 4, 2)
contador(78, 9, 45, 90, 36)'''

'''def contador(*num):
    for valor in num:
        print(f'{valor}' , end=' ')
    print('Fim!')
        
    
contador(2, 1, 7)
contador(3, 7, 8, 4, 2)
contador(78, 9, 45, 90, 36)'''

'''def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')
        
    
contador(2, 1, 7)
contador(3, 7, 8, 4, 2)
contador(78, 9, 45, 90, 36)'''

'''def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos]  *= 2
        pos += 1
        
valores = [4, 8, 9, 10, 56, 39]
dobra(valores)
print(valores)'''

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)