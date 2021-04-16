#teste try and except

#PROGRAMA CALCULAR MÉDIA ALUNO, COM CONTORNO DE ERRO!!!

nota = input('digite uma nota: ')
nota_1 = input('digite outra nota: ')

try:
    nota = float(nota)
    nota_1 = float(nota_1)
    media_nota = (nota + nota_1) / 2

    if media_nota >= 9:
        print(f'APROVADO com louvor, a sua média foi {media_nota}!')
    elif media_nota >= 7:
        print(f'APROVADO, a sua média foi {media_nota}')
    elif media_nota >= 5:
        print(f'RECUPERAÇÃO, a sua média foi {media_nota}!')
    else:
        print(f'REPROVADO, a sua média foi {media_nota}!')

except:
    print('ERROR!!')