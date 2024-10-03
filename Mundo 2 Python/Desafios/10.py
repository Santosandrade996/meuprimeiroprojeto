#Jokenpo

import random

def jogar_jokenpo(escolha_jogador):
    opcoes = ['pedra', 'papel', 'tesoura']
    escolha_computador = random.choice(opcoes)

    print("O computador escolheu:", escolha_computador)

    if escolha_jogador == escolha_computador:
        return "Empate!"
    elif (escolha_jogador == 'pedra' and escolha_computador == 'tesoura') or \
         (escolha_jogador == 'papel' and escolha_computador == 'pedra') or \
         (escolha_jogador == 'tesoura' and escolha_computador == 'papel'):
        return "Você ganhou!"
    else:
        return "Você perdeu!"

def main():
    print("Bem-vindo ao Jokenpo! Escolha pedra, papel ou tesoura.")

    escolha_jogador = input("Digite sua escolha: ").lower()

    if escolha_jogador not in ['pedra', 'papel', 'tesoura']:
        print("Escolha inválida. Por favor, escolha pedra, papel ou tesoura.")
        return

    resultado = jogar_jokenpo(escolha_jogador)
    print(resultado)

main()
