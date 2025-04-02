'''valores = []

while True:
    num = int(input('Digite um valor númerico: ( Ou -1 para parar):'))
    if num == -1:
        break
    if num in valores:
        valores.append(num)
    else:
        print('Esse número já foi adicionado.')
valores.sort()
print('Valores que foram adiconados...')'''

'''lista = []
while True:
    num = int(input("Digite um valor numerico (0 para parar): "))
    if num == 0:
        break
    if num not in lista:
        lista.append(num)

print("Valores digitados em ordem crescente:", sorted(lista))'''

valores = []

while True:
    num = int(input("Digite um número (ou -1 para sair): "))
    
    if num == -1:
        break
    
    if num in valores:
        print("Esse número já foi adicionado. Tente novamente!")
    else:
        valores.append(num)
        print("Número adicionado com sucesso.")

valores.sort()  
print("Valores únicos digitados:", valores)


