#varios números 
contador = 0  
soma = 0
maior = None
menor = None

while True:
    numero = int(input('Digite um número inteiro:'))
    
    contador += 1
    soma += numero
    
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero
        
    continuar = input('Quer continuar? (S/N):').strip().upper()
    if continuar == 'N':
        break
    
if contador > 0:
    media = soma / contador
    print(f'Você digitou {contador} números.')
    print(f'A média dos valores digitados é {media:.2f}.')
    print(f'O maior valor digitado foi {maior}.')
    print(f'O menor valor digitado foi {menor}.')
else:
    print('Nenhum número foi digitado...')
    