# imprecisão de pontos flutuantes
# Double-precision floating-point format IEEE 754

numero_1 = 0.2
numero_2 = 0.3
numero_3 = numero_1 + numero_2
print(f'{numero_3:.2f}')
# ou
print(round(numero_3, 2))



import decimal

numero_1 = decimal.Decimal(0.2)
numero_2 = decimal.Decimal(0.3)
numero_3 = numero_1 + numero_2
print(round(numero_3, 3))
