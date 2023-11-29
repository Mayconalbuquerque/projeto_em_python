# Função Lambda em Python
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única expressão.


# lista = [
#     4, 23, 1, 32, 4, 5, 6, 6, 
# ]

# lista.sort(key=ordenar)
# lista.sort(reverse = True)
# sorted(lista)


lista = [
    {'Nome': 'Maycon', 'Sobrenome': 'Albuquerque'},
    {'Nome': 'Fatima', 'Sobrenome': 'Pereira'},
    {'Nome': 'Rodrigo', 'Sobrenome': 'Morais'},
    {'Nome': 'Rafael', 'Sobrenome': 'Morais'},
    {'Nome': 'Amaro', 'Sobrenome': 'Albuquerque'},
    {'Nome': 'Veronica', 'Sobrenome': 'Albuquerque'},
]

# lista = [
#     4, 23, 1, 32, 4, 5, 6, 6, 
# ]

# def ordenar(item):
#     return item['Nome']

# lista.sort(key=ordenar)
# lista.sort(reverse = True)
# sorted(lista)

# for item in lista:
#     print(item)


# or 

# lista.sort(key=lambda item: item['Nome'])

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key = lambda item: item['Nome'])
l2 = sorted(lista, key = lambda item: item['Sobrenome'])

exibir(l1)
exibir(l2)

#CÓPIA RASA
