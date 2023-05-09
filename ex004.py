# Dissecando uma variável- Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas
# as informações possiveis sobre eles.
a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É Alfabetico?', a.isalpha())
print('É Alfanúmerico?', a.isalnum())
print('Ésta em MAIÚSCULAS?', a.isupper())
print('Ésta em minúsculas?', a.islower())
print('Ésta capitalizada?', a.istitle())



