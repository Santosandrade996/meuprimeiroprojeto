#Area
def area(largura, comprimento):
    terreno = largura * comprimento
    print(f'A área do terreno de {largura} x {comprimento} é {terreno} m².')
    
    
largura = float(input("Digite a largura do terreno (m):"))
comprimento = float(input("Digite a altura do terreno (m):"))

area(largura, comprimento)

