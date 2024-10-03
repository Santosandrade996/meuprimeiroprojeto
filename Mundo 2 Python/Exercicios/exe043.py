#Massa corporal

peso = float(input('Informe o seu peso (em KG!):'))
altura = float(input('Digite sua altura (em Metros):'))
imc = peso / (altura ** 2) 
print('O IMC é de {:.2f}' .format(imc))

if imc < 18.5:
    print('Você esta abaixo do PESO normal!')
elif 18.5 <= imc < 25:                         #Calculo matematico que python  aceita...
    print('Você esta com o seu PESO IDEAL!')
elif 25<= imc < 30:
    print('Sobrepeso!')
elif 30 <= imc < 40:
    print('OBESIDADE!')
else:
    print('Você está com OBESIDADE MÓRBIDA!')
    
