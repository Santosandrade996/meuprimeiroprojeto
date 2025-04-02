#Parte 2
jogadores = []

while True:
    
    jogador = {}  
    jogador['nome'] = input("Digite o nome do jogador: ")
    num_partidas = int(input(f"Digite a quantidade de partidas que {jogador['nome']} jogou: "))

    
    gols_por_partida = []

   
    for partida in range(1, num_partidas + 1):
        gols = int(input(f"Digite a quantidade de gols na partida {partida}: "))
        gols_por_partida.append(gols)

    
    jogador['gols_por_partida'] = gols_por_partida
    jogador['total_gols'] = sum(gols_por_partida)  

   
    jogadores.append(jogador)

   
    continuar = input("Deseja cadastrar outro jogador? [S/N]: ").strip().lower()
    if continuar != 's':
        break


print("\n=============================================")
print("         <<< Informações dos jogadores >>>     ")
print("=============================================")
for j in jogadores:
    print(f"Nome: {j['nome']}")
    print(f"Partidas jogadas: {len(j['gols_por_partida'])}")
    print(f"Gols por partida: {j['gols_por_partida']}")
    print(f"Total de gols no campeonato: {j['total_gols']}")
    print("---------------------------------------------")
