pessoas = []
total_idade = 0
mulheres = []

while True:
    pessoa = {}
    
    pessoa['nome'] = input("Digite o nome: ")
    pessoa['idade'] = int(input("Digite a idade: "))
    pessoa['sexo'] = input("Digite o sexo [M/F]: ").strip().upper()

    # Adicionando a idade à soma total
    total_idade += pessoa['idade']

    # Verificando se é mulher
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    
    # Adicionando a pessoa à lista de pessoas
    pessoas.append(pessoa)
    
    # Perguntando se deseja continuar
    continuar = input("Deseja cadastrar mais alguma pessoa? [S/N]: ").strip().upper()
    if continuar == 'N':
        break

# Cálculo da média de idade
total_pessoas = len(pessoas)
media_idade = total_idade / total_pessoas if total_pessoas > 0 else 0

# Inicializando a lista de pessoas acima da média
pessoas_acima_media = []

# Verificando pessoas acima da média
for p in pessoas:
    if p['idade'] > media_idade:
        pessoas_acima_media.append(p)

# Exibindo os resultados
print("=================================================")
print(f" Total de pessoas cadastradas: {total_pessoas}")
print(f" Média de idade do grupo: {media_idade:.2f}")
print(" Lista de mulheres cadastradas:", mulheres if mulheres else "Nenhuma mulher cadastrada")
print(" Lista de pessoas com idade acima da média:")

if pessoas_acima_media:  
    for p in pessoas_acima_media:
        print(f"   - {p['nome']}, {p['idade']} anos")
else:
    print("   Nenhuma pessoa com idade acima da média.")
