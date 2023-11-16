<<<<<<< HEAD
# Manipulando chaves e valores em dicionários
import os

pessoa = {}


pessoa['nome'] = 'Maycon'
pessoa['sobrenome'] = 'Albuquerque'


os.system('cls')

print(pessoa)
print()
print(pessoa['sobrenome'])
=======
# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'


print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai')
>>>>>>> 9fb9588f8d5259ae0e834699afa6d08f178fc99a
