#Valores inteiros

def maior(*valores):
    if len(valores) == 0:
        print('Nenhum valor foi passado!')
        return
    
    maior_valor = max(valores) #Chamando a função max() para retornar o valor maior
    print(f'O maior valor é {maior_valor}')


maior(3, 5, 7, 2, 8, 4)
maior(10, 20, 30, 40, 50, 60 , 70)
maior()