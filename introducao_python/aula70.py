frase = 'Python é uma linguagem de programação'\
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'

# numero_letras = frase.count('a')

# print(numero_letras)

i = 0
qntd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):

    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue

    quantas_vezes_letra_aparece = frase.count(letra_atual)

    if qntd_apareceu_mais_vezes < quantas_vezes_letra_aparece:
        qntd_apareceu_mais_vezes = quantas_vezes_letra_aparece
        letra_apareceu_mais_vezes = letra_atual

i += 1
print(
    'A letra que apareceu mais vezes foi '
    f'{letra_apareceu_mais_vezes} que apareceu '
    f'{qntd_apareceu_mais_vezes}x'
)