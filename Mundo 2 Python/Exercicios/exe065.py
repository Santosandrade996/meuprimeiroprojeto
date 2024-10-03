#Maior e menores valores 
resposta = 'S'
soma = quantidade = media = maior = menor = 0 #forma mais ismplificada das variaveis
while resposta in 'Ss':
    numero = int(input('Digite um número:'))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
                menor = numero
    resposta = str(input('Quer continuar? [S/N]')).upper().strip() [0]
media = soma / quantidade
print(f'Você digitou {quantidade} e a media foi {media}')
print(f'O maior valor foi {maior} e o menor {menor}')
