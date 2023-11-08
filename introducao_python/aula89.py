# enumerate = enumera iteráveis(índices)

lista = ['Maria', 'João', 'José']
lista.append('Maycon')


# lista_enumerada = enumerate(lista)

# print(lista_enumerada)

# for item in lista_enumerada:
#     print(item)

for tupla_enumerada in enumerate(lista):
    print('\n')
    for valor in tupla_enumerada:
        print(f'{valor}')
        