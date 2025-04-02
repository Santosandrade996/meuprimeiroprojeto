import random

def sorteio(): #Função Sorteio()
    numeros = [random.randint(1, 100) for _ in range(5)] 
    print(f'Números sorteados são: {numeros}')
    return numeros


def somapar(numeros):
    soma = sum(num for num in numeros if num % 2 == 0) #Somatorio só de números pares
    print(f'Soma dos números pares sorteados: {soma}')
    

numeros = sorteio() # Chama a função sorteio() e acaba armazenando os números neles que estão sorteados
somapar(numeros) # chama a função somaPar() vai fazer só o somatorio dos pares

