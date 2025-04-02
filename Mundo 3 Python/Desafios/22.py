# Parte 1
jogador = {}


jogador['nome'] = input("Digite o nome do jogador: ")
num_partidas = int(input("Digite a quantidade de partidas que ele jogou: "))


gols_por_partida = []

for partida in range(num_partidas):
    gols = int(input(f"Digite a quantidade de gols na partida {partida + 1}: "))
    gols_por_partida.append(gols)


jogador['gols_por_partida'] = gols_por_partida
jogador['total_gols'] = sum(gols_por_partida)  

# Exibindo as informações coletadas
print("\n=============================================")
print("         <<<Informações do jogador>>>        ")
print("=============================================")
print(f"Nome: {jogador['nome']}")
print(f"Partidas jogadas: {num_partidas}")
print(f"Gols por partida: {jogador['gols_por_partida']}")
print(f"Total de gols no campeonato: {jogador['total_gols']}")
