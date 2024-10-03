#Condições Aninhadas
#nome = str(input('Qual é o seu nome?'))  #Esses codigos desenvolvidos se chama condição simples
#if nome == 'Giselle':
#  print('Nome bonito!')
#print('Tenha umm bom dia, {}!'.format(nome))


#2- Condições composta
#nome = str(input('Qual é o seu nome?'))
#if nome == 'Giselle':
#  print('Que nome bonito!')
#else:
#  print('Seu nome é bem feio!')
#print('Tenha um bom dia, {}!'.format(nome))

#Estrutura aninhada
nome = str(input('Qual é o seu nome?'))
if nome == 'Giselle':
    print('Seu nome é bonito!')
elif nome == 'Maria' or nome == 'João' or nome == 'Jão' or nome == 'jujuba':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Juliano periquito fofoqueiro':
    print('Que belos nomes!')
else:
    print('Seu nome é feio!')
print('Tenha um bom dia, {}!'.format(nome))
