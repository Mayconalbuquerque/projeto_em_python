# Lista de lista e seus índices

salas = [
    ['Maria', 'Helena', ],

    ['Helaine',],

    ['Luiz', 'João', 'Eduarda', ],
                                    #tupla
]

# print(salas[1][0])

for sala in salas:
    # print(sala)
    for aluno in sala:
        print(aluno)