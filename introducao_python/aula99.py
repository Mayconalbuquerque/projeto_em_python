# Calculo do segundo dígito do CPF
# cpf : 838.697.760-48
# Colete a soma dos 9 primeiros digitos do CPF,
# MAIS O PRIMEIRO DIGITO,
# multiplicando cada um dos valores por uma
# contagem regressiva começando de 11

# Ex:  838.697.760-48 (838697760)
#     11  10  9   8   7   6   5   4   3  2
# *   8   3   8   6   9   7   7   6   0  4 <-- PRIMEIRO DIGITO
#     88  30  72  48  63  42  35  24  0  8

# Somar todos os resultados: 
# 88 + 30 + 72 + 48 + 63 + 42 + 35 + 24 + 0 + 8 = 410
# Multiplicar o resultado anterior por 10

# 410 * 10 = 4100

# Obter o resto da divisão da conta anterior por 11

# 410 % 11 = 0

# Se o resultado anterior for maior que 9:
#     resultado é 0

# Contrário disso:
#     resultado é o valor da conta

# O segundo dígito do CPF é 8



cpf = '838.697.760-48' \
    .replace('.', '') \
    .replace('.', '') \
    .replace('.', '') \
    .replace('-', '')

nove_digitos_1 = cpf[:9]
contador_1 = 10

resultado_1 = 0

for digito1 in nove_digitos_1:
    resultado_1 += (int(digito1) * contador_1)
    contador_1 -= 1

valor_final_1 = ((resultado_1 * 10) % 11)
primeiro_digito = valor_final_1 if valor_final_1 <= 9 else 0

dez_digitos_2 = nove_digitos_1 + str(primeiro_digito)
contador_2 = 11

resultado_2 = 0

for digito2 in dez_digitos_2:
    resultado_2 += (int(digito2) * contador_2)
    contador_2 -= 1

valor_final_2 = ((resultado_2 * 10) % 11)
segundo_digito = valor_final_2 if valor_final_2 <= 9 else 0

cpf_gerado = f'{nove_digitos_1}{primeiro_digito}{segundo_digito}'

if cpf == cpf_gerado:
    print(f'o CPF {cpf} é válido.')
else:
    print('CPF é inválido.')