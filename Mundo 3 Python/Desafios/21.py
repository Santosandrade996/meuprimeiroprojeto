# Aviso sobre aposentadoria
print('-=' * 40)
print('<<<      Carteira de Trabalho e Providência Social (CTPS)        >>>')
print('-=' * 40)

aviso = (
    "==============================================================================================\n"
    "                  AVISO IMPORTANTE SOBRE APOSENTADORIA\n"
    "================================================================================================================================\n"
    "A idade mínima para se aposentar por idade no INSS em 2024 é de 62 anos e 6 meses para homens e 65 anos e 6 meses para mulheres.\n"
    "Para ambos os sexos, é necessário ter contribuído para o INSS por pelo menos 15 anos.\n"
    "Para trabalhadores rurais, a idade mínima é reduzida em 5 anos para homens e 7 anos para mulheres.\n"
    "O registro na carteira de trabalho (CTPS) é presumido como verdadeiro e serve como prova do vínculo empregatício,\n"
    "com efeitos previdenciários.\n"
    "================================================================================================================================="
)

# Centralizando o texto
largura = 60  # Definindo a largura do terminal
print(aviso.center(largura))

from datetime import datetime
trabalhador = {}

trabalhador['nome'] = input("Digite o nome: ")
trabalhador['ano_nascimento'] = int(input("Digite o ano de nascimento: "))

trabalhador['idade'] = datetime.now().year - trabalhador['ano_nascimento']  # Calculando a idade
trabalhador['ctps'] = int(input("Digite o número da CTPS (0 se não tiver): "))


if trabalhador['ctps'] != 0:
    trabalhador["ano_contratacao"] = int(input("Digite o ano de contratação: "))
   
   
    while True:
        try:
            trabalhador['salario'] = float(input("Digite o salário: "))  
            break  
        except ValueError:
           
            print("Por favor, insira um valor numérico válido para o salário.")
            
            
            
    
    if trabalhador['idade'] < 65:  # Para homens
        anos_aposentadoria = 65 - trabalhador['idade']
        anos_contribuicao = 15 - (2024 - trabalhador["ano_contratacao"])
        if anos_contribuicao < 0:
            anos_contribuicao = 0
        trabalhador['aposentadoria'] = (anos_aposentadoria, anos_contribuicao)
    
    elif trabalhador['idade'] < 62:  # Para mulheres
        anos_aposentadoria = 62 - trabalhador['idade']
        anos_contribuicao = 15 - (2024 - trabalhador["ano_contratacao"])
        if anos_contribuicao < 0:
            anos_contribuicao = 0
        trabalhador['aposentadoria'] = (anos_aposentadoria, anos_contribuicao)

else:
    # Se não tiver CTPS, informar sobre a necessidade de contribuição
    print("\nPara se aposentar, você precisa contribuir para o INSS.")
    if trabalhador['idade'] < 65:  # Para homens
        anos_aposentadoria = 65 - trabalhador['idade']
        print(f"Você ainda precisa de {anos_aposentadoria} anos para se aposentar por idade.")
    
    elif trabalhador['idade'] < 62:  # Para mulheres
        anos_aposentadoria = 62 - trabalhador['idade']
        print(f"Você ainda precisa de {anos_aposentadoria} anos para se aposentar por idade.")

#Informações coletadas 
print("         <<< Informações do trabalhador: >>>         ")
print('-='  * 30)

for chave, valor in trabalhador.items():
    if chave == 'aposentadoria':
        print(f"A aposentadoria: {valor[0]} anos até a aposentadoria e {valor[1]} anos de contribuição restantes.")
     
    elif chave == 'salario':
        print(f"{chave.capitalize()}: R$ {valor:.2f}")  
    elif chave == "ano_contratacao":
        print(f'Ano de contratação: {valor}')
    else:
        print(f"{chave.capitalize()}: {valor}")
        
        
        
   
        