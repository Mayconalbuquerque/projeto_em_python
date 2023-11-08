"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2   10  9  8  7  6  5  4  3  2   
*  7   4  6  8  2  4  8  9  0   3   8  5  3  5  5  2  0  8 
   70  36 48 56 12 20 32 27 0   30  72 

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""


cpf = '38535520805'
nove_digitos = cpf[:9]
contador_1 = 10

resultado_1 = 0

for digito1 in nove_digitos:
    resultado_1 += (int(digito1) * contador_1)
    contador_1 -= 1

valor_final_1 = ((resultado_1 * 10) % 11)
primeiro_digito = valor_final_1 if valor_final_1 <= 9 else 0
