from math import radians, sin, cos, tan

an = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(an))
print('O angulo de {} tem o SENO de {:.2f}'.format(an, seno))
cosseno = cos(radians(an))
print('O angulo de {} tem o COSSENO de {:.2f} ' .format(an,  cosseno))
tangente = tan(radians(an))
print('O angulo de {}  tem a TANGENTE de {:.2f}' .format(an, tangente))
# Seno, cosseno e tangente.



