#Media aritmetica v.2

nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
media = (nota1 + nota2) /2
print('Tirando {:.1f} e {:.1f} a media do aluno sera {:.1f}' .format(nota1, nota2, media))

#if media >=5 and media < 7:
    #print('O aluno está de Recuperação!')

#Outa maneira de se fazer este codigo acima
if 7 > media >=5:
    print('O aluno está de recuperação!')
elif media < 5:
    print('O aluno está Reprovado!')
elif media >=7:
    print('O aluno está Aprovado!')