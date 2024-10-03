#Desconto

def calcular_valor_produto(preco, forma_pagamento, parcelas):
    if forma_pagamento == 'dinheiro' or forma_pagamento == 'cheque':
        return preco * 0.9  #10% de desconto
    elif forma_pagamento == 'cartao' and parcelas == 1:
        return preco * 0.95  #5% de desconto
    elif forma_pagamento == 'cartao' and parcelas == 2:
        return preco  #preço normal
    elif forma_pagamento == 'cartao' and parcelas >= 3:
        return preco * 1.2  #20% de desconto
    else:
        return 'Condição de pagamento inválida!'


def main():
    preco = float(input('Digite o preço do produto:'))
    forma_pagamento = input('Digite a forma de pagamento (dinheiro, cheque ou cartao):').lower()
    parcelas = int(input("Digite o número de parcelas (ou 1 para pagamento à vista): "))

    valor_a_pagar = calcular_valor_produto(preco, forma_pagamento, parcelas)
    print('O valor a ser pago é {:.2f}'.format(valor_a_pagar))


main()
