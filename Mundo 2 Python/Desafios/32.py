#Tabuada com interrupção break
'''print('-=' * 10)
print('Tabuada')
print('-=' * 10)

while True:
    numero = int(input('Digite qualquer número para mostrar a tabuada: [Sabendo qua número negativo finaliza a tabuada!]'))
    
    if numero < 0:
        break
    
    print(f'Tabuada do {numero}:')
    i = 1
    
    while True:
        print(f'{numero} x {i} = {numero * i}')
        i += 1
        continue = input('Deseja continuar? [S/N]?')
        break
    print()
        
        
        
print('Programa encerrado...')'''

while True:
    # Pede ao usuário para digitar um número
    numero = int(input("Digite um número para ver a tabuada (número negativo para parar): "))
    
    # Verifica se o número é negativo para interromper o programa
    if numero < 0:
        break
    
    # Mostra a tabuada do número digitado
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print()  # Linha em branco para separar as tabuadas

print("Programa encerrado.")

