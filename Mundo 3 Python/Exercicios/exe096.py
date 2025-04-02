#Função que calcula área

def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de  {a}m²')    


#Programa principal
print('Controle de Terrenos')
print('-' * 20)
l = float(input('Largura (m²):'))
c = float(input('Comprimento (m²):'))
area(l, c)
