valores = []

for _ in range(5):
    num = int(input('Digite um número:'))
    
    pos = 0
    while pos < len(valores) and valores[pos] < num:
        pos += 1
        
    valores.insert(pos, num)
    
print('Lista ordenada:', valores)
