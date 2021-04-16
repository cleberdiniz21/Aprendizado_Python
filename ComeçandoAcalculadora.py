a = 'Calculadora'
print(f'{a.upper():*^50}')
print()

valor = input('Digite a tabuada a ser calculada: ')

contador = 0
valor = valor

try:  # o try vai tentar executar o programa.

    if valor.isnumeric():
        pass

        while contador < 10:

            valor = int(valor)
            contador = contador + 1
            multi = contador * valor

            print(f'{valor:2} x {contador:2d} = {multi:2}')

    else:
        print('Digite um número inteiro.')

except:  # Se algo der errado, apresenta está msg.
    print('Digite um número inteiro.')
