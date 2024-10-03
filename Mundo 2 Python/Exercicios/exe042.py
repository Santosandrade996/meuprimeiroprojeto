# Analisando triangulo V.2
lado1 = float(input('Primeiro segmento:'))
lado2 = float(input('Segundo segmento:'))
lado3 = float(input('Terceiro segmento:'))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os segmentos acima podem formar triangulo!' , end= ' ')
    if lado1 == lado2 == lado3:
        print('Equilátero')
    elif lado1 != lado2 != lado3 and lado3 != lado1:
        print('Esacaleno')
    else:
        print('Isoceles!')
else:
    print('Eles não podem formar um triangulo!')
 