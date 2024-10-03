
#Triangulos

def verificar_tipo_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return 'Equilatero'
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return 'Isoceles'
    else:
        return 'Escaleno'


def main():
    lado1 = float(input('Digite o comprimento do primeiro lado:'))
    lado2 = float(input('Digite o comprimento do segundo lado:'))
    lado3 = float(input('Digite o comprimento do terceiro lado:'))

    tipo_triangulo = verificar_tipo_triangulo(lado1, lado2, lado3)
    print('O triangulo formado é do tipo:', tipo_triangulo)


main()

