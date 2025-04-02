# vogais 

palavras = ('Caderno', 'Lapiseira', 'Apontador', 'Quadro', 'Amarelinha', 'Recreio', 'Comida', 'Ensinar', 'Sucesso')

def extrair_vogais(palavra):
    return [letra for letra in palavra.lower() if letra in 'aeiou'] #Dentro da condiçao joguei para maiusculas.


for palavra in palavras:
    vogais = extrair_vogais(palavra)
    print(f"As vogais na palavra '{palavra}' são: {', ' .join(vogais)}")
    
    
    