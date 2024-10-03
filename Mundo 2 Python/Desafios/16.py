#Progressão artmetica

primeiro_termo = float(input('Digite o primeiro termo da progressão aritmética: '))
razao = float(input('Digite a razão da progressão artmética são:'))
print('Os 10 primeiros termos da progressão artmética são:'
)

for i in range(10):
    termo = primeiro_termo + i * razao
    print(termo)
