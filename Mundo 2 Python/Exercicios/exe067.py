#Tabuada v3.0
print('-=' * 20)
print('Tabuada V3.0')
print('-=' * 20)

while True:
    n = int(input('Quer ver a tabuadad de qual valor?'))
    if n < 0:
        break
    print('-=' * 30)
    for c in range(1,11):
        print(f'{n} x {c} = {n * c}')
    print('-=' * 30)
    
print('Tabuada encerrada...Volte Sempre!')
