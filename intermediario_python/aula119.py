'''
Dicionários em Python(tipo dict)

Dicionários são estruturas de dados do tipo
par de "Chave" e "Valor".

Chaves podem ser consideradas como o "Índice"
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc.

O valor pode ser de qualquer tipo, incluindo outro
dicionário.

Usamos as chaves - {} - ou a classe dict para criar
dicionários.

Imutáveis: str, int, float, bool, tuple
Mutável: dict, list

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
    {'rua': 'rua da cerâmica', 'número': 123},
    {'rua': 'rua anny', 'número': 209},
    ],
}
'''

# pessoa = {
#     'nome': 'Maycon',
#     'sobrenome': 'Albuquerque',
# }

# pessoa = dict(nome='Maycon', sobrenome='Albuquerque')

# print(pessoa, type(pessoa))

import os

pessoa = {
    'nome': 'Maycon',
    'sobrenome': 'Albuquerque',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
    {'rua': 'rua da cerâmica', 'número': 123},
    {'rua': 'rua anny', 'número': 209},
    ],
}
os.system('cls')
# print(pessoa['nome'])

for chave in pessoa:
    print(chave, pessoa[chave])