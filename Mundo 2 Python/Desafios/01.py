#Emprestimo bancario

casa = float(input('Valor total da casa: R$'))
salario = float(input('Slario do empregador recebido por mês: R$'))
anos = int(input('Quantos anos de financiamento:'))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {}' .format(casa, anos))
print('A prestação será de R${:.2f}' .format(prestacao))

if prestacao <= minimo:
    print('Emprestimo concedido!')
else:
    print('Emprestimo negado!')
            
   
