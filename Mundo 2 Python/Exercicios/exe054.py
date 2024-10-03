#Analisador de idades de pessoas
from datetime import date

atual = date.today().year
total_maior = 0
total_menor = 0

for pessoa in range(1,8):    
    nascimento = int(input('Em que ano a {}º pessoa nasceu?' .format(pessoa)))
    idade = atual - nascimento

    if idade >=21:
        total_maior += 1
    else:
       total_menor += 1
print(f'Ao Todo tivemos {total_maior} pessoas maiores de idade, e tambem tivemos {total_menor} pessoas menores de idade')