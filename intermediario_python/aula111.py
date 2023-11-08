# args - argumento não nomeados
# *args (empacotamento e desempacotamento)

# Lembre-se de desempacotamento

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)


# def soma(*args):
#     total = 0

#     for numeros in args:
#         total += numeros
#         print('Total', total)

# soma(1, 2, 3, 4, 5, 6)

def soma(*args):
    total = 0

    for numeros in args:
        total += numeros
        print('Soma:', numeros)
        print('Total', total)

soma(1, 2, 3, 4, 5, 6)