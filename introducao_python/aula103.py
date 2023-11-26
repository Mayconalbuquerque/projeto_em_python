# Criando um gerador de cpf's

import random

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0, 9))

contador_1 = 10

resultado_1 = 0

for digito1 in nove_digitos:
    resultado_1 += (int(digito1) * contador_1)
    contador_1 -= 1

valor_final_1 = ((resultado_1 * 10) % 11)
primeiro_digito = valor_final_1 if valor_final_1 <= 9 else 0

dez_digitos_2 = nove_digitos + str(primeiro_digito)
contador_2 = 11

resultado_2 = 0

for digito2 in dez_digitos_2:
    resultado_2 += (int(digito2) * contador_2)
    contador_2 -= 1

valor_final_2 = ((resultado_2 * 10) % 11)
segundo_digito = valor_final_2 if valor_final_2 <= 9 else 0

cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

print(cpf_gerado)
