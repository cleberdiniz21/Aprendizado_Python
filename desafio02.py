#Desafio número 02

d = (input('Digite um número inteiro! '))

if d.isdigit():
    d = int(d)

    if d % 2 == 0:
        print(f'{d} é par!!! ')
    else:
        print(f'{d} é ímpar!!! ')
else:
    print('Isso não é um número inteiro, '
          'digite outro número!')





