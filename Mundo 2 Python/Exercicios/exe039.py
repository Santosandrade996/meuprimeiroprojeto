#Alistamento militar
from datetime import date


print('''
[1] Masculino
[2] Feminino''')

sexo = int(input('Digite o número correspondente ao seu sexo: '))

if sexo == 1:
    ano_atual = date.today().year
    ano_nascimento = int(input('Qual seu ano de nascimento? '))
    idade = ano_atual - ano_nascimento
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nascimento, idade, ano_atual))

    if idade == 18:
        print('Você tem que se alistar imediatamente!')
    elif idade < 18:
        saldo = 18 - idade
        print('Você ainda não tem 18 anos. Faltam {} anos para se alistar!'.format(saldo))
        ano = ano_atual + saldo
        print('Seu alistamento será em {}.'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você deveria ter se alistado há {} anos!'.format(saldo))
        ano = ano_atual - saldo
        print('Seu alistamento foi em {}.'.format(ano))

elif sexo == 2:
    print('Você não é obrigada a se alistar no serviço militar.')

else:
    print('Entrada inválida. Por favor, digite "1" para Masculino ou "2" para Feminino.')
    