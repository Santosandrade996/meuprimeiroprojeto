# Dobro, Triplo e Raiz quadrada
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1 / 2)
print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}.  \nA Raiz quadrada de {} é igual a {:.2f}. '.format(n, t, n, r))
# Outra maneira de se fazer:
n = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(n, (n * 2)))
print('O triplo de {} vale {}. \nA Raiz quadrada de {} é igual a {:.2f}.'.format(n, (n * 3), n, (n ** (1 / 2))))
# Fazendo com outra função:
n = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(n, (n * 2)))
print('O triplo de {} vale {}. \nA Raiz quadrada de {} é igual a {:.2f}.'.format(n, (n * 3), n, pow(n, (1 / 2))))
