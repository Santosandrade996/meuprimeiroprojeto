valores = [] #Vai ler varios números
pares = [] #Criando 2 listas que é pares e ímpares
impares = []

while True:
    num = int(input('Digite um número (ou -1 para sair):'))
    
    if num == -1:
        break
    
    valores.append(num) #Adicionando  os números da lista principal
    
    if num % 2 == 0:
        pares.append(num) #Vai adicionar a lista de pares
        
    else:
        impares.append(num) #Vai adicionar a lista de ímpares
        
#Ordenando os valores para ficar direito       
valores.sort()
pares.sort()
impares.sort()
        
print(f'\nLista de todos os valores: {valores}')
print(f'Lista de valores pares: {pares}')
print(f'Lista de valores ímpares: {impares}')
 