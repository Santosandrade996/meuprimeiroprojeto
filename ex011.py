# Calculando area e altura para saber a quantidade de tinta necessaria.
larg = float(input('largura da parede:'))
alt = float(input('Altura da parde: '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m². '.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta. ' .format(tinta))




