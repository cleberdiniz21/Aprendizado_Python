print('Cálculo de Bhaskara')
print()
import math
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

x = ((-1 * b) + (math.sqrt(b**2 - 4 * a * c))) / 2 * a

print(f'A raiz da equação é {x}')

