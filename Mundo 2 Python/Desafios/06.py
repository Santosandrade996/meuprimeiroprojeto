#Natação
def determinar_categoria(ano_nascimento):
    idade = 2024 - ano_nascimento

    if idade <= 9:
        return 'mirim'
    elif idade <= 14:
        return 'infantil'
    elif idade <= 19:
        return 'junior'
    elif idade <= 20:
        return 'sênior'
    else:
        return 'master'


def main():
    ano_nascimento = int(input('Digite o ano de nascimento do atleta:'))

    categoria = determinar_categoria(ano_nascimento)
    print('A categoria do atleta é:', categoria)


main()

