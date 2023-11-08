# Calculadora com while

while True:
    num_1 = input('Digite um numero: ')
    num_2 = input('Digite outro numero: ')
    operador = input('Informe um operador (+-/*): ')
    numero_operadores = len(operador)
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos: ')
        continue
    
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    if numero_operadores > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando a sua conta, confira o resultado abaixo: ')
    if operador == '+':
        print(f'{num_1_float } + {num_2_float} = {num_1_float + num_2_float}')
    
    elif operador == '-':
        print(f'{num_1_float } - {num_2_float} = {num_1_float - num_2_float}')

    elif operador == '*':
        print(f'{num_1_float } x {num_2_float} = {num_1_float * num_2_float}')

    elif operador == '/':
        print(f'{num_1_float } / {num_2_float} = {num_1_float / num_2_float}')

    else:
        print('Nunca deveria chegar aqui.')

    sair = input('Você deseja sair? [S]im ou [N]ão')
    sair = sair.lower()
    
    
    if sair == 's':
        print('saindo')

    else:
        continue
