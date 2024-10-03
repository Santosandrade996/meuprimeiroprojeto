#Peso

def calculo_imc(peso, altura):
    return peso / (altura ** 2)


def determinar_status(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif 18.5 <= imc < 25:
        return 'Peso ideal'
    elif 25 <= imc < 30:
        return 'Sobrepeso'
    elif 30 <= imc < 40:
        return 'Obesidade'
    else:
        return 'Obesidade morbida'


def main():
    peso = float(input('Digite o peso (em kg):'))
    altura = float(input('Digite a altura (em metros): '))

    imc = calculo_imc(peso, altura)
    status = determinar_status(imc)
    print("o IMC é", imc)
    print("Status:", status)


main()

