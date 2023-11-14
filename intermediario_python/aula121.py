"""
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shalllow copy)
get - obtém a chave
pop - Apaga o último item adicionado
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro
"""

pessoa = {
    'nome': 'Maycon',
    'sobrenome': 'Albuquerque',
}

# print(pessoa.__len__())

# print(len(pessoa))

# print(list(pessoa.keys()))

# for valores in pessoa.keys():
#     print(valores)

print(list(pessoa.values()))

print(list(pessoa.items()))

for nome, sobrenome in pessoa.items:
    print(nome, sobrenome)