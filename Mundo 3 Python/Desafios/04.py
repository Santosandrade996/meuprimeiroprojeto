#Quatro valores
valores = (
    int(input('Digite o primeiro valor:')),
    int(input('Digite o segundo valor:')),
    int(input('Digite o terceiro valor:')),
    int(input('Digite o quarto valor: '))
)

contagem_nove = valores.count(9)
posicao_tres = valores.index(3) if 3 in valores else None

numeros_pares  = [num for num in valores if num % 2 == 0]

print(f'\nO número 9 aparece {contagem_nove} tantas vezes.')
if posicao_tres is not None:
    print(f'o primeiro valor 3 foi digitado na posição {posicao_tres}.')
else:
    print(f'O valor 3 não foi digitado...')
print(f'Números pares digitados são: {numeros_pares}')
