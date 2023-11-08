def calculadora():
    operacao = input('''
Selecione o tipo de operação que deseja realizar:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

    number_1 = input('Digite o primeiro numero: ')
    number_2 = input('Digite o segundo numero: ')
    
    number_1_float = float(number_1)
    number_2_float = float(number_2)
    
    if number_1.isdigit() and number_2.isdigit():

        if operacao == '+':
            print('{} + {} = '.format(number_1, number_2))
            print(number_1_float + number_2_float)
    
        elif operacao == '-':
            print('{} - {} = '.format(number_1, number_2))
            print(number_1_float - number_2_float)
    
        elif operacao == '*':
            print('{} * {} = '.format(number_1, number_2))
            print(number_1_float * number_2_float)
    
        elif operacao == '/':
            print('{} / {} = '.format(number_1, number_2))
            print(number_1_float / number_2_float)
    
        else:
            print('Você digitou um operador inválido. Por favor reinicie o programa.')
    
    else:
        print('Você digitou um numero inválido. Por favor reinicie o programa.')

    
    repetir()

def repetir():
    calc_novamente = input('''
Você deseja calcular novamente?
Digite S para SIM e N para Não.
''')

    if calc_novamente.upper() == 'S':
        calculadora()
    elif calc_again.upper() == 'N':
        print('Até mais.')
    else:
        repetir()

calculadora()