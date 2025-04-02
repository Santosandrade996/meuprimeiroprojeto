#contador

from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:  # Corrige passo 0 para evitar erro
        passo = 1
    if passo < 0:  # Transforma passo negativo para contagem reversa
        passo = -passo

    print(f"Contando de {inicio} até {fim} de {abs(passo)} em {abs(passo)}:")
    sleep(1)

    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=" ", flush=True)
            sleep(0.3)
    else:
        for i in range(inicio, fim - 1, -passo):
            print(i, end=" ", flush=True)
            sleep(0.3)
    print("FIM!")
    print("=" * 30)

# A) Contagem de 1 até 10, de 1 em 1
contador(1, 10, 1)

# B) Contagem de 10 até 0, de 2 em 2
contador(10, 0, 2)

# C) Contagem personalizada (somente após pedir os valores ao usuário)
print("Agora é a sua vez de personalizar a contagem!")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)

