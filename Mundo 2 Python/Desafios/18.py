# Palindromo 

# Solicita ao usuário que insira uma frase
frase_usuario = input("Digite uma frase: ")

# Remove os espaços da frase e converte para letras minúsculas
frase_sem_espacos = frase_usuario.replace(" ", "").lower()

# Verifica se a frase sem espaços é igual à sua inversa
if frase_sem_espacos == frase_sem_espacos[::-1]:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")
