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


# print(perguntas[0]['Pergunta'])
# print(perguntas[0]['Opções'])
# resposta = 'Digite a sua resposta: '
# resposta_correta = 4

# for opcao in perguntas[0]['Opções']:
#     print(opcao)

# print(resposta)

# if resposta == resposta_correta:
#     print('Você acertou!')

# else:
#     ('Você errou!')

def pergunta_1(perguntas):
    print(perguntas[0]['Pergunta'])
    print(perguntas[0]['Opções'])
    resposta = input('Digite a sua resposta: ')
    resposta_correta = '4'
    if resposta == resposta_correta:
        print('Você acertou!')

    else:
        print('Você errou!')

print(pergunta_1(perguntas)) 

