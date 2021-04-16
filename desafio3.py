#Desafio 03

#nome = input('Digite seu nome? ')
#dig = float(input('Digite um horário 0.00-23.59! '))


#if dig >= 0.00 and dig <= 11.59:
#    print(f"Bom dia {nome} ")
#
#elif dig >= 12.00 and dig <= 17.59:
#        print(f'Boa tarde {nome}')

#elif dig >=18.00 and dig <= 23.59:
#    print(f'Boa noite {nome}')

horario = input('Digite um horário(0-23): ')

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print('Horário deve estar entre 0 e 23')
    else:
        if horario <= 11:
            print('Bom dia!')
        elif horario <= 17:
            print("Boa tarde")
        else:
            print ('Boa noite')
else:
    print('Por favor digite um horário entre 0 e 23.')

