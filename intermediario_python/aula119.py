<<<<<<< HEAD
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
=======
# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Maycon',
#     'sobrenome': 'Albuquerque',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')
pessoa = {
    'nome': 'Maycon',
    'sobrenome': 'Albuquerque',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
# print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
>>>>>>> 9fb9588f8d5259ae0e834699afa6d08f178fc99a
    print(chave, pessoa[chave])