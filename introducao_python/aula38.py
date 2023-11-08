#faça um programa que leia 2 valores e informe qual é o maior valor

first_value = int(input('Digite um número'))
second_value = int(input('Digite outro número '))

if first_value > second_value:
    print(f'Primeiro valor: {first_value:.2f} é maior que o segundo valor: {second_value:.2f}.')

elif first_value == second_value:
    print(f'Primeiro valor: {first_value:.2f} e o segundo valor: {second_value:.2f} são iguais.')

else:
    print(f'O segundo valor: {second_value:.2f} é maior que o primeiro valor: {first_value:.2f}.')
