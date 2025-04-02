#Contando vogais em tuplas

palavras = ('Caderno', 'Lapiseira', 'Apontador', 'Quadro', 'Amarelinha', 'Recreio', 'Comida', 'Ensinar', 'Sucesso')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos:', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')