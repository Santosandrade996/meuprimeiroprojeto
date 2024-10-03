#Definições de sexo
print('=' * 250)

print('\033[91mCisgênero: é a pessoa que se identifica com o sexo biológico designado no momento de seu nascimento.')
print('\033[93mTransgênero: é quem se identifica com um gênero diferente daquele atribuído no nascimento.')
print('\033[94mNão-binário: é alguém que não se identifica completamente com o “gênero de nascença” nem com outro gênero. Esta pessoa pode não se ver em nenhum dos papéis comuns associados aos homens e as mulheres bem como pode vivenciar uma mistura de ambos.')

print('=' * 250)

sexo = input('Digite o sexo desejado (C/T/N):').upper()

while sexo not in ['C' , 'T', 'N']:
    print(" \033[91mValor inválido! Por favor, digite 'C', 'T', ou 'N'.")
    sexo = input("Digite o gênero da pessoa (C/T/N):").upper()
    
print('Gênero registrado com sucesso...')