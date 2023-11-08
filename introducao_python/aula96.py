# Desempacotamento de chamadas
# de métodos e funções

string = 'ABCD'

lista = ['Maycon', 'Pereira', 1, 2 , 3, 'Albuquerque']

tupla = 'Python', '2023'

#p, b, c, *_, u = lista

#print(p, u)

for nome in lista:
    print(nome, end = ' ')

#ou


#print(*lista)

salas = [
    ['Maycon', 'Lucas'],
    ['Vitória', ],
    ['Ana', 'Heloisa', ],
]

print(salas)
print(*salas)
print(*salas, sep = '\n')