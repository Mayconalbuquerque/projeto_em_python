# Exercícios com funçõe

# Crie uma função que multiplica todos os argumentos
# nao nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uma função fala se um número é par ou ímpar.
# Retorne seo número é par ou impar.

def multiplicacao(*args):
    total = 1

    for numero in args:
        total = total * numero
    return total

numeros = 4, 4
outra_multiplicacao = multiplicacao(*numeros)
print(outra_multiplicacao)