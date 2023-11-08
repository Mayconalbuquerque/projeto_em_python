#formatação da string

nome = str(input('Digite o seu nome: '))
altura = float(input('Digite a sua altura em metros: '))
peso = float(input('Digite o seu peso em quilos: '))
imc = peso / altura ** 2

#:.2f = 2 casas decimais com . (90.90)
#:,2f = 100,050.40

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'
 
print(linha_1)
print(linha_2)
print(linha_3)
    