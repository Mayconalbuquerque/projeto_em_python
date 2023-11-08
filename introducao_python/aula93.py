# slip e join com list e str
# split - divide uma string
# join - une uma string
# strip - apaga os espaços

frase = 'Eu tenho um cachorro'
lista_palavras = frase.split()

lista = []
for i, frase in enumerate(lista_palavras):
    lista.append(lista_palavras[i].strip())
    # print(lista_palavras[i].strip())

print(lista)

frases_unidas = '-'.join(abc)
print(frases_unidas)