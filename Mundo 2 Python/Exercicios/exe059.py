from time import sleep

n1 = int(input('Primeir valor:'))
n2 = int(input('Segundo valor:'))
opcão = 0

while opcão != 5:
    print('''   
        Menu
        [1]Somar
        [2]Multiplicar
        [3]Maior
        [4]Novos números
        [5]Sair do programa
        ''')
    opcão = int(input('>>>>> Qual é a sua opção?'))
    if opcão == 1:
       soma = n1 + n2
       print(f'A soma entre {n1} + {n2} é igual a: {soma}') 
    elif opcão == 2:
        Multiplicação = n1 * n2
        print(f'A multiplicação entre {n1} x {n2} é igual a {Multiplicação}')
    elif opcão == 3:
        if n1 > n2:
           maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif opcão == 4:
        print('Informe os números novamente...')
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
    elif opcão ==5:
        print('Finalizando...')
    else:
        print('Opção Invalida! Tente Novamente....')
    
    sleep(2)
print('Fim do programa...Volte Sempre!')
