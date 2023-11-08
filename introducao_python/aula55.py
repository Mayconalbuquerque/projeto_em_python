# Solução 1 
# enunciados


# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou impar. Caso o usuário não digite um número
# inteiro, informe que não é um número inteiro.


entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0 
    par_impar_texto = 'Ímpar'
    
    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada} é {par_impar_texto}')

else:
    print('Você não digitou um número inteiro')




# Solução 2

# Faça um programa que pergunte a hora ao usuário e,
# baseando-se no horário descrito, exiba a saudação apropriada.
# Ex.
# Bom dia 0-11, Boa Tarde 12-17 e Boa noite 18-23.



horas = input('Digite o horário\nExemplo: 12.20\n: ')

try:

    horas_float = float(horas)
    
    if horas_float >= 00 and horas_float <= 11:
        print('Bom dia!')
    
    elif horas_float >= 12 and horas_float <= 17:
        print('Boa tarde!')
    
    elif horas_float >= 18 and horas_float <= 23:
        print('Boa noite!')

    else:
        print('Hora não reconhecida')

except:
    print('Desculpe, ocorreu um erro! Tente novamente.')


# Solução 3


nome = input('Digite um nome: ')
tam_nome = len(nome)

if tam_nome > 1 :
    if tam_nome <= 4:
        print('Seu nome é curto')
    
    elif tam_nome >= 5 and tam_nome <= 6:
        print('Seu nome é normal.')
    
    else:
        print('Seu nome é muito grande.')

else:
    print('Digite mais que uma letra.')