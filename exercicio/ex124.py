'''
Exercício - sistema de perguntas e respostas
'''



perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for perguntas in perguntas:
    print('Pergunta:', perguntas['Pergunta'])
    print()

    for i, opcoes in enumerate(perguntas['Opções']):
        print(f'{i})', opcoes)
    print()

    escolha = input('Escolha uma opção: ')

    break