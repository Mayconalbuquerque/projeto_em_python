# Exercícios com funçõe

# Crie uma função que multiplica todos os argumentos
# nao nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uma função fala se um número é par ou ímpar.
# Retorne seo número é par ou impar.

def multiplication(*args):
    total = 1

    for number in args:
        total = total * number
    return total

numbers = 1, 2, 3
last_multiplier = multiplication(*numbers)
print(last_multiplier)

if (last_multiplier % 2) == 0:
    print('This number is even!')

else:
    print('This number is odd') 