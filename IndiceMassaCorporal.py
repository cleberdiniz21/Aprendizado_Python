#Cálculo Massa Corporal
print()
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
resultado = peso / (altura * altura)

if resultado < 18.5:
    print(f"Abaixo do peso, O seu IMC é {resultado}.")
elif resultado >= 18.5 and resultado <=24.9:
    print(f"Peso norma, O seu IMC é {resultado}.")
elif resultado >=25 and resultado <= 29.9:
    print(f"Sobrepeso, O seu IMC é {resultado}.")
elif resultado >=30 and resultado <= 34.9:
    print(f"Obesidade Grau I, O seu IMC é {resultado}.")
elif resultado >=35 and resultado <= 39.9:
    print(f"Obesidade Grau II, O seu IMC é {resultado}.")
else:
    print(f"Obesidade Grau III, O seu IMC é {resultado}.")

