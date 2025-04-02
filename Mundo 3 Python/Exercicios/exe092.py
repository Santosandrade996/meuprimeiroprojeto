#Cadastro do Trabalhador
from datetime import datetime

dados = dict()
dados['nome'] = str(input('Nome: '))
dados['nascimento'] = int(input('Digite o ano de nascimento: '))
dados['idade'] = datetime.now().year - dados['nascimento']
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

print('=' * 30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}:')