from datetime import datetime


def verificar_alistamento(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento

    if idade < 18:
        anos_faltantes = 18 - idade
        return "Você ainda vai se alistar ao serviço militar. Faltam {} anos.".format(anos_faltantes)
    elif idade == 18:
        return "É hora de se alistar ao serviço militar!"
    else:
        anos_passados = idade - 18
        return "Você já passou do tempo de se alistar ao serviço militar. Passaram {} anos.".format(anos_passados)


def main():
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    resultado = verificar_alistamento(ano_nascimento)
    print(resultado)


main()
