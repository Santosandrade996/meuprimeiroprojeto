# Analise de texto

nome = str(input('Digite o nome completo: ')).strip()
# Usando a função strip retorna a lista das strings s usando caracteres
# em branco como separadores...
print('Analisando seu nome...')
print('Seu nome em MAIÚSCULAS é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
# Função upper() é para converter dentro de uma string para maiúscula.
# Função lower() é para converter dentro de uma string para minúsculas.
print('Seu nome tem ao todo {} de letras'.format(len(nome) - nome.count(' ')))
# E usando a função -nome.count para eliminar os espaços...
# Utilizando nome.find para saber quantas letras tem o primeiro nome:
# print('Seu primeiro nome tem {} de letras'.format(nome.find(' ')))
separa = nome.split()
# Split() é utilizado para manipulações de strings e divide o conteúdo da variável.
print('Seu primeiro nome é {} e ele tem {} de letras'.format(separa[0], len(separa[0])))



