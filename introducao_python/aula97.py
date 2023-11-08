# Operação ternária (condicional de uma linha)
# <valor> if <condição> else <outro valor>

# print('Valor' if True else 'Outro valor.')


# condicao = 100 == 111

# variavel = 'Valor verdadeiro' if True else 'Outro valor'

# print(variavel)

digito = 9
# novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)