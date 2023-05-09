# Custo da viagem
distancia = float(input('Qual é a distância da sua viagem? '))
print('Vcê está prestes a começar uma viagem de {}km.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45

print('E o preço da sua passagem será de R${:.2f}'.format(preço))
# Identação simples...
# distancia = float(input('Qual é a distância da sua viagem? '))
# print('Vcê está prestes a começar uma viagem de {}km.' .format(distancia))
# preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
# print('E o preço da sua passagem será de R${:.2f}'.format(preço))


