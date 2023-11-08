# introdução ao try/except
# try - tentar executar o código
# except - ocorreu algum erro ao tentar executar

# print(1234)
# print(5678)
# int('abcde')

# try:
#     print(12345)
#     print(678910)
#     int('abcde')
#     print('Não aparecerá no console')

# except:
#     print('Você digitou algo errado!')


numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')
